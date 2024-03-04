#!/usr/bin/env python
""" Electromagnetic simulation using the FDTD method """


import sys

import numpy as np
from PyQt6 import QtWidgets

import sources
import visualize


def main():

	ke = 200
	ex = np.zeros(ke)
	hy = np.zeros(ke)

	Ex, Hy = sources.pulse(ke, ex, hy)

	app = QtWidgets.QApplication(sys.argv)
	window = visualize.MainWindow(Ex, Hy)
	window.show()
	sys.exit(app.exec())

if __name__ == "__main__":
	main()
