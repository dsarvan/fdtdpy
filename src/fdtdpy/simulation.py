#!/usr/bin/env python
""" FDTD simulation """

import numpy as np

import sources
import medium as md


def simulate(ke: int, ex: np.ndarray, hy: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Finite-difference time-domain method

    :param int ke: number of electric and magnetic field nodes
    :param np.ndarray ex: electric field oriented in the x direction
    :param np.ndarray hy: magnetic field oriented in the y direction

    :return: Ex, Hy: stack of electric and magnetic field
    :rtype: tuple[np.ndarray, np.ndarray]

    """

    nsteps: int = 1500

    # free space absorbing boundary condition
    lbound = [0, 0] # boundary low
    hbound = [0, 0] # boundary high

    # propagation in a lossy dielectric medium
    ca, cb = md.dielectric(ke, ddx=0.01, epsr=4, sigma=0.04)

    Ex = np.empty((0, ex.shape[0]))
    Hy = np.empty((0, hy.shape[0]))

    # FDTD simulation loop
    for t in range(1, nsteps + 1):
        # calculate the Ex field
        ex[1:ke] = ca[1:ke] * ex[1:ke] + cb[1:ke] * (hy[0:ke-1] - hy[1:ke])

        # sinusoidal wave source (frequency 700 MHz)
        ex[1] = ex[1] + sources.sinusoidal(t, freq=700e6)

        # absorbing boundary conditions
        ex[0], lbound[0], lbound[1] = lbound[0], lbound[1], ex[1]
        ex[ke-1], hbound[0], hbound[1] = hbound[0], hbound[1], ex[ke-2]

        # calculate the Hy field
        hy[0:ke-1] = hy[0:ke-1] + 0.5 * (ex[0:ke-1] - ex[1:ke])

        Ex = np.vstack((Ex, ex))
        Hy = np.vstack((Hy, hy))

    return Ex, Hy
