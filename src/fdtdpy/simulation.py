#!/usr/bin/env python
""" FDTD simulation """

import numpy as np

import sources


def simulate(ke: int, ex: np.ndarray, hy: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Finite-difference time-domain method

    :param int ke: number of electric and magnetic field nodes
    :param np.ndarray ex: electric field oriented in the x direction
    :param np.ndarray hy: magnetic field oriented in the y direction

    :return: Ex, Hy: stack of electric and magnetic field
    :rtype: tuple[np.ndarray, np.ndarray]

    """

    nsteps: int = 500

    lbound = [0, 0]
    hbound = [0, 0]

    Ex = np.empty((0, ex.shape[0]))
    Hy = np.empty((0, hy.shape[0]))

    # FDTD simulation loop
    for t in range(1, nsteps + 1):
        # calculate the Ex field
        ex[1:ke] = ex[1:ke] + 0.5 * (hy[0:ke-1] - hy[1:ke])

        # sinusoidal wave source (frequency 1900 MHz)
        ex[1] = ex[1] + sources.sinusoidal(t, freq=1900e6)

        # absorbing boundary conditions
        ex[0], lbound[0], lbound[1] = lbound[0], lbound[1], ex[1]
        ex[ke-1], hbound[0], hbound[1] = hbound[0], hbound[1], ex[ke-2]

        # calculate the Hy field
        hy[0:ke-1] = hy[0:ke-1] + 0.5 * (ex[0:ke-1] - ex[1:ke])

        Ex = np.vstack((Ex, ex))
        Hy = np.vstack((Hy, hy))

    return Ex, Hy
