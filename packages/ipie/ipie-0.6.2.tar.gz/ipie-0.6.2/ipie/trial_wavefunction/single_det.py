import numpy as np
import time

from ipie.config import config
from ipie.estimators.generic import half_rotated_cholesky_jk
from ipie.estimators.greens_function_batch import (
    greens_function_single_det,
    greens_function_single_det_batch,
)
from ipie.estimators.utils import gab_spin
from ipie.propagation.overlap import (
    calc_overlap_single_det_batch,
)
from ipie.propagation.force_bias import (
    construct_force_bias_batch_single_det_chunked,
    construct_force_bias_batch_single_det,
)
from ipie.trial_wavefunction.wavefunction_base import TrialWavefunctionBase
from ipie.trial_wavefunction.half_rotate import half_rotate_generic


class SingleDet(TrialWavefunctionBase):
    def __init__(self, wavefunction, num_elec, num_basis, verbose=False):
        assert isinstance(wavefunction, np.ndarray)
        assert len(wavefunction.shape) == 2
        super().__init__(wavefunction, num_elec, num_basis, verbose=verbose)
        if verbose:
            print("# Parsing input options for trial_wavefunction.MultiSlater.")
        self.psi = wavefunction
        self.num_elec = num_elec
        self._num_dets = 1
        self._max_num_dets = 1
        imag_norm = np.sum(self.psi.imag.ravel() * self.psi.imag.ravel())
        if imag_norm <= 1e-8:
            # print("# making trial wavefunction MO coefficient real")
            self.psi = np.array(self.psi.real, dtype=np.float64)

        self.psi0a = self.psi[:, : self.nalpha]
        self.psi0b = self.psi[:, self.nalpha :]
        self.G, self.Ghalf = gab_spin(self.psi, self.psi, self.nalpha, self.nbeta)

    def build(self) -> None:
        pass

    @property
    def num_dets(self) -> int:
        return 1

    @num_dets.setter
    def num_dets(self, ndets: int) -> None:
        raise RuntimeError("Cannot modify number of determinants in SingleDet trial.")

    def calculate_energy(self, system, hamiltonian) -> np.ndarray:
        if self.verbose:
            print("# Computing trial wavefunction energy.")
        start = time.time()
        self.e1b = (
            np.sum(self.Ghalf[0] * self._rH1a)
            + np.sum(self.Ghalf[1] * self._rH1b)
            + hamiltonian.ecore
        )
        self.ej, self.ek = half_rotated_cholesky_jk(
            system, self.Ghalf[0], self.Ghalf[1], trial=self
        )
        self.e2b = self.ej + self.ek
        self.energy = self.e1b + self.e2b

        if self.verbose:
            print(
                "# (E, E1B, E2B): (%13.8e, %13.8e, %13.8e)"
                % (self.energy.real, self.e1b.real, self.e2b.real)
            )
            print("# Time to evaluate local energy: {} s".format(time.time() - start))

    def half_rotate(self, system, hamiltonian, comm=None):
        num_dets = 1
        orbsa = self.psi0a.reshape((num_dets, self.nbasis, self.nalpha))
        orbsb = self.psi0b.reshape((num_dets, self.nbasis, self.nbeta))
        rot_1body, rot_chol = half_rotate_generic(
            self,
            system,
            hamiltonian,
            comm,
            orbsa,
            orbsb,
            ndets=num_dets,
            verbose=self.verbose,
        )
        # Single determinant functions do not expect determinant index, so just
        # grab zeroth element.
        self._rH1a = rot_1body[0][0]
        self._rH1b = rot_1body[1][0]
        self._rchola = rot_chol[0][0]
        self._rcholb = rot_chol[1][0]
        self.half_rotated = True

    def calc_overlap(self, walkers) -> np.ndarray:
        return calc_overlap_single_det_batch(walkers, self)

    def calc_greens_function(self, walkers, build_full=False) -> np.ndarray:
        if config.get_option("use_gpu"):
            return greens_function_single_det_batch(walkers, self, build_full=build_full)
        else:
            return greens_function_single_det(walkers, self, build_full=build_full)

    def calc_force_bias(self, hamiltonian, walkers, mpi_handler=None) -> np.ndarray:
        if hamiltonian.chunked:
            return construct_force_bias_batch_single_det_chunked(
                hamiltonian, walkers, self, mpi_handler
            )
        else:
            return construct_force_bias_batch_single_det(hamiltonian, walkers, self)

    # def cast_to_single_precision(self):
    # assert self._rchola is not none
    # self._vbias0 = self._rchola.dot(self.psi0a.t.ravel()) + self._rchola.dot(
    # self.psi0b.t.ravel()
    # )
    # self._rchola = self._rchola.astype(np.float32)
    # self._rcholb = self._rcholb.astype(np.float32)
