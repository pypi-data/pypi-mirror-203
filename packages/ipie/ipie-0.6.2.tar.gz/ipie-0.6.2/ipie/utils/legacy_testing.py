import copy
from dataclasses import dataclass
import numpy as np
from typing import Tuple, Union

from ipie.legacy.qmc.afqmc import AFQMC
from ipie.legacy.propagation.continuous import Continuous as LegacyContinuous
from ipie.legacy.walkers.single_det import SingleDetWalker
from ipie.legacy.trial_wavefunction.multi_slater import MultiSlater
from ipie.legacy.walkers.handler import Walkers
from ipie.legacy.estimators.local_energy import local_energy_generic_cholesky_opt

from ipie.utils.testing import (
    generate_hamiltonian,
    get_random_nomsd,
    get_random_phmsd_opt,
)
from ipie.utils.misc import dotdict
from ipie.hamiltonians.generic import Generic as HamGeneric
from ipie.systems.generic import Generic


def build_legacy_test_case(
    wfn,
    init,
    system,
    ham,
    num_steps,
    num_walkers,
    dt,
    nstblz=5,
):
    qmc = dotdict({"dt": dt, "nstblz": nstblz})
    options = {"hybrid": True}
    ham_legacy = copy.deepcopy(ham)
    ham_legacy.control_variate = False
    trial = MultiSlater(system, ham_legacy, wfn, init=init)
    trial.half_rotate(system, ham_legacy)
    if trial.ndets == 1:
        trial.psi = trial.psi[0]
    prop = LegacyContinuous(system, ham_legacy, trial, qmc, options=options)

    walkers = [SingleDetWalker(system, ham_legacy, trial) for iw in range(num_walkers)]
    for i in range(num_steps):
        for walker in walkers:
            prop.propagate_walker(walker, system, ham_legacy, trial, 0.0)
            _ = walker.reortho(trial)  # reorthogonalizing to stablize
            walker.greens_function(trial)
    return walkers


def get_legacy_walker_energies(system, ham, trial, walkers):
    etots = []
    e1s = []
    e2s = []
    for iw, walker in enumerate(walkers):
        e = local_energy_generic_cholesky_opt(
            system,
            ham,
            walker.G[0],
            walker.G[1],
            walker.Ghalf[0],
            walker.Ghalf[1],
            trial._rchola,
            trial._rcholb,
        )
        etots += [e[0]]
        e1s += [e[1]]
        e2s += [e[2]]
    return etots, e1s, e2s


@dataclass(frozen=True)
class LegacyTestData:
    trial: MultiSlater
    walker_handler: Walkers
    hamiltonian: HamGeneric
    propagator: LegacyContinuous


def build_legacy_test_case_handlers_mpi(
    num_elec: Tuple[int, int],
    num_basis: int,
    mpi_handler,
    num_dets=1,
    trial_type="phmsd",
    complex_integrals: bool = False,
    complex_trial: bool = False,
    seed: Union[int, None] = None,
    rhf_trial: bool = False,
    two_body_only: bool = False,
    options={},
):
    if seed is not None:
        np.random.seed(seed)
    assert len(options) > 0
    h1e, chol, enuc, eri = generate_hamiltonian(
        num_basis, num_elec, cplx=complex_integrals
    )
    system = Generic(nelec=num_elec)
    ham_legacy = HamGeneric(
        h1e=np.array([h1e, h1e]),
        chol=chol.reshape((-1, num_basis**2)).T.copy(),
        ecore=0,
        options={"symmetry": False},
    )
    ham_legacy.control_variate = False
    ham_legacy.stochastic_ri = False
    ham_legacy.pno = False
    ham_legacy.control_variate = False

    if trial_type == "phmsd":
        wfn, init = get_random_phmsd_opt(
            num_elec[0],
            num_elec[1],
            num_basis,
            ndet=num_dets,
            init=True,
            cmplx_coeffs=complex_trial,
        )
    else:
        coeffs, slater_mats, init = get_random_nomsd(
            num_elec[0], num_elec[1], num_basis, num_dets, cplx=complex_trial, init=True
        )
        wfn = (coeffs, slater_mats)

    trial = MultiSlater(system, ham_legacy, wfn, init=init)
    trial.half_rotate(system, ham_legacy)
    trial.calculate_energy(system, ham_legacy)
    if trial.ndets == 1:
        trial.psi = trial.psi[0]
        if rhf_trial:
            trial.psi[:, num_elec[0] :] = trial.psi[:, : num_elec[0]]
    # necessary for backwards compatabilty with tests
    if seed is not None:
        np.random.seed(seed)
    options.ntot_walkers = options.nwalkers * mpi_handler.comm.size
    prop = LegacyContinuous(system, ham_legacy, trial, options, options=options)
    handler = Walkers(
        system,
        ham_legacy,
        trial,
        options,
        options,
        verbose=False,
        comm=mpi_handler.comm,
    )
    for i in range(options.num_steps):
        for walker in handler.walkers:
            if two_body_only:
                prop.two_body_propagator(walker, system, ham_legacy, trial)
            else:
                prop.propagate_walker(walker, system, ham_legacy, trial, trial.energy)
            _ = walker.reortho(trial)  # reorthogonalizing to stablize
            walker.greens_function(trial)
        handler.pop_control(mpi_handler.comm)

    return LegacyTestData(trial, handler, ham_legacy, prop)


def build_legacy_test_case_handlers(
    num_elec: Tuple[int, int],
    num_basis: int,
    num_dets=1,
    trial_type="phmsd",
    complex_integrals: bool = False,
    complex_trial: bool = False,
    rhf_trial: bool = False,
    seed: Union[int, None] = None,
    two_body_only: bool = False,
    options={},
):
    if seed is not None:
        np.random.seed(seed)
    assert len(options) > 0
    h1e, chol, enuc, eri = generate_hamiltonian(
        num_basis, num_elec, cplx=complex_integrals
    )
    system = Generic(nelec=num_elec)
    ham_legacy = HamGeneric(
        h1e=np.array([h1e, h1e]),
        chol=chol.reshape((-1, num_basis**2)).T.copy(),
        ecore=0,
        options={"symmetry": False},
    )
    ham_legacy.control_variate = False
    ham_legacy.stochastic_ri = False
    ham_legacy.pno = False

    if trial_type == "phmsd":
        wfn, init = get_random_phmsd_opt(
            num_elec[0],
            num_elec[1],
            num_basis,
            ndet=num_dets,
            init=True,
            cmplx_coeffs=complex_trial,
        )
    else:
        coeffs, slater_mats, init = get_random_nomsd(
            num_elec[0], num_elec[1], num_basis, num_dets, cplx=complex_trial, init=True
        )
        if rhf_trial:
            assert num_dets == 1
            slater_mats[0, :, num_elec[0] :] = slater_mats[0, :, : num_elec[0]]
            init[:, num_elec[0] :] = init[:, : num_elec[0]]
        wfn = (coeffs, slater_mats)

    trial = MultiSlater(system, ham_legacy, wfn, init=init)
    trial.half_rotate(system, ham_legacy)
    trial.calculate_energy(system, ham_legacy)
    if trial.ndets == 1:
        trial.psi = trial.psi[0]
    # necessary for backwards compatabilty with tests
    if seed is not None:
        np.random.seed(seed)
    prop = LegacyContinuous(system, ham_legacy, trial, options, options=options)
    handler = Walkers(
        system,
        ham_legacy,
        trial,
        options,
        options,
        verbose=False,
    )
    for i in range(options.num_steps):
        for walker in handler.walkers:
            if two_body_only:
                prop.two_body_propagator(walker, system, ham_legacy, trial)
            else:
                prop.propagate_walker(walker, system, ham_legacy, trial, trial.energy)
            _ = walker.reortho(trial)  # reorthogonalizing to stablize
            walker.greens_function(trial)

    return LegacyTestData(trial, handler, ham_legacy, prop)


def build_legacy_driver_instance(
    num_elec: Tuple[int, int],
    num_basis: int,
    num_dets=1,
    trial_type="phmsd",
    complex_integrals: bool = False,
    complex_trial: bool = False,
    rhf_trial: bool = False,
    seed: Union[int, None] = None,
    density_diff: bool = False,
    options={},
):
    if seed is not None:
        np.random.seed(seed)
    assert len(options) > 0
    h1e, chol, enuc, eri = generate_hamiltonian(
        num_basis, num_elec, cplx=complex_integrals
    )
    system = Generic(nelec=num_elec)
    ham_legacy = HamGeneric(
        h1e=np.array([h1e, h1e]),
        chol=chol.reshape((-1, num_basis**2)).T.copy(),
        ecore=0,
        options={"symmetry": False},
    )
    ham_legacy.control_variate = False
    ham_legacy.stochastic_ri = False
    ham_legacy.pno = False

    if trial_type == "phmsd":
        wfn, init = get_random_phmsd_opt(
            num_elec[0],
            num_elec[1],
            num_basis,
            ndet=num_dets,
            init=True,
            cmplx_coeffs=complex_trial,
        )
    else:
        coeffs, slater_mats, init = get_random_nomsd(
            num_elec[0],
            num_elec[1],
            num_basis,
            num_dets,
            cplx=complex_trial,
            init=True,
        )
        if rhf_trial:
            assert num_dets == 1
            slater_mats[0, :, num_elec[0] :] = slater_mats[0, :, : num_elec[0]]
            init[:, num_elec[0] :] = init[:, : num_elec[0]]
        wfn = (coeffs, slater_mats)

    trial = MultiSlater(system, ham_legacy, wfn)
    trial.half_rotate(system, ham_legacy)
    trial.calculate_energy(system, ham_legacy)
    if trial.ndets == 1:
        trial.psi = trial.psi[0]

    from mpi4py import MPI

    comm = MPI.COMM_WORLD
    afqmc = AFQMC(
        comm=comm,
        system=system,
        hamiltonian=ham_legacy,
        options=options,
        trial=trial,
    )
    afqmc.estimators.estimators["mixed"].print_header()

    return afqmc
