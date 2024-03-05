#!/usr/bin/env python
""" Simulation sources """

import numpy as np


def pulse(ke: int, ex: np.ndarray, hy: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Gaussian pulse source

    :param int ke: number of electric and magnetic field nodes
    :param np.ndarray ex: electric field oriented in the x direction
    :param np.ndarray hy: magnetic field oriented in the y direction

    :return: Ex, Hy: stack of electric and magnetic field
    :rtype: tuple[np.ndarray, np.ndarray]

    """

    # pulse parameters
    kc: int = ke // 2
    t0: int = 40
    spread: float = 12
    nsteps: int = 500

    lbound = [0, 0]
    hbound = [0, 0]

    Ex = np.empty((0, ex.shape[0]))
    Hy = np.empty((0, hy.shape[0]))

    # FDTD loop
    for time_step in range(1, nsteps + 1):
        # calculate the Ex field
        ex[1:ke] = ex[1:ke] + 0.5 * (hy[0:ke-1] - hy[1:ke])

        # put a Gaussian pulse in the middle
        ex[1] = ex[1] + np.exp(-0.5 * ((t0 - time_step) / spread) ** 2)

        # absorbing boundary conditions
        ex[0], lbound[0], lbound[1] = lbound[0], lbound[1], ex[1]
        ex[ke-1], hbound[0], hbound[1] = hbound[0], hbound[1], ex[ke-2]

        # calculate the Hy field
        hy[0:ke-1] = hy[0:ke-1] + 0.5 * (ex[0:ke-1] - ex[1:ke])

        Ex = np.vstack((Ex, ex))
        Hy = np.vstack((Hy, hy))

    return Ex, Hy


def sinusoidal(
    ke: int, ex: np.ndarray, hy: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """
    Sinusoidal wave source

    :param int ke: number of electric and magnetic field nodes
    :param np.ndarray ex: electric field oriented in the x direction
    :param np.ndarray hy: magnetic field oriented in the y direction

    :return: Ex, Hy: stack of electric and magnetic field
    :rtype: tuple[np.ndarray, np.ndarray]

    """

    # wave parameters
    ddx: float = 0.01
    dt: float = ddx / 6e8
    freq: float = 700e6
    nsteps: int = 500

    lbound = [0, 0]
    hbound = [0, 0]

    Ex = np.empty((0, ex.shape[0]))
    Hy = np.empty((0, hy.shape[0]))

    # FDTD loop
    for time_step in range(1, nsteps + 1):
        # calculate the Ex field
        ex[1:ke] = ex[1:ke] + 0.5 * (hy[0:ke-1] - hy[1:ke])

        # put a sinusoidal wave in the middle
        ex[1] = ex[1] + np.sin(2 * np.pi * freq * dt * time_step)

        # absorbing boundary conditions
        ex[0], lbound[0], lbound[1] = lbound[0], lbound[1], ex[1]
        ex[ke-1], hbound[0], hbound[1] = hbound[0], hbound[1], ex[ke-2]

        # calculate the Hy field
        hy[0:ke-1] = hy[0:ke-1] + 0.5 * (ex[0:ke-1] - ex[1:ke])

        Ex = np.vstack((Ex, ex))
        Hy = np.vstack((Hy, hy))

    return Ex, Hy
