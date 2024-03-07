#!/usr/bin/env python
""" Electromagnetic simulation using the FDTD method """


import sys

import numpy as np
from PyQt6 import QtWidgets

import sources
import visualize


def main():
    """FDTD method"""

    ke = 200
    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    #Ex, Hy = sources.pulse(ke, ex, hy)
    Ex, Hy = sources.sinusoidal(ke, ex, hy)

    app = QtWidgets.QApplication(sys.argv)
    window = visualize.MainWindow(Ex, Hy)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    sys.exit(main())
