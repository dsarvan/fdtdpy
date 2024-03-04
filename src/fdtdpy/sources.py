#!/usr/bin/env python
""" Simulation sources """

import numpy as np


def pulse(ke, ex, hy):
    """Gaussian pulse source

    Args:
            ke: number of electric and magnetic field nodes
            ex: electric field oriented in the x direction
            hy: magnetic field oriented in the y direction

    Returns:
            Ex, Hy: stack of electric and magnetic field

    """

    # pulse parameters
    kc = ke // 2
    t0 = 40
    spread = 12
    nsteps = 500

    Ex = np.empty((0, ex.shape[0]))
    Hy = np.empty((0, hy.shape[0]))

    # FDTD loop
    for time_step in range(1, nsteps + 1):

        # calculate the Ex field
        for k in range(1, ke):
            ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])

        # put a Gaussian pulse in the middle
        ex[kc] = np.exp(-0.5 * ((t0 - time_step) / spread) ** 2)

        # calculate the Hy field
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

        Ex = np.vstack((Ex, ex))
        Hy = np.vstack((Hy, hy))

    return Ex, Hy
