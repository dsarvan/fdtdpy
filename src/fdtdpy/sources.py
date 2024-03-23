#!/usr/bin/env python
""" Simulation sources """

import numpy as np


def gaussian(t: int, t0: int = 70, sigma: float = 12) -> float:
    """
    Gaussian pulse source

    :param int t: an integer counter that serves as the temporal index
    :param int t0: time step at which gaussian function is maximum, default 40
    :param float sigma: width of the gaussian pulse, default 12

    :return: gaussian pulse
    :rtype: float

    """

    return np.exp(-0.5 * ((t - t0) / sigma) ** 2)


def sinusoidal(t: int, ddx: float = 0.01, freq: float = 700e6) -> float:
    """
    Sinusoidal wave source

    :param int t: an integer counter that serves as the temporal index
    :param float ddx: the cell size (m), default 0.01 m
    :param float freq: frequency of the sinusoidal wave source, default 700 MHz

    :return: sinusoidal wave
    :rtype: float

    """

    dt: float = ddx / 6e8  # time step

    return np.sin(2 * np.pi * freq * dt * t)
