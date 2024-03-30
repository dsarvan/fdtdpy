#!/usr/bin/env python
""" Material medium """

import numpy as np


def dielectric(ke, epsr: int = 1, sigma: float = 0.04, ddx: float = 0.01):
	"""
	Dielectric medium

	:param int ke: number of electric and magnetic field nodes
	:param int epsr: relative dielectric constant, default 1
	:param float sigma: conductivity, default 0.04
	:param float ddx: the cell size (m), default 0.01 m

	"""

	eps0 = 8.854e-12
	dt = ddx/6e8

	ca = np.ones(ke)
	cb = 0.5 * np.ones(ke)

	eaf = dt * sigma/(2 * eps0 * epsr)

	ca[ke//2:] = (1 - eaf)/(1 + eaf)
	cb[ke//2:] = 0.5/(epsr * (1 + eaf))

	return ca, cb
