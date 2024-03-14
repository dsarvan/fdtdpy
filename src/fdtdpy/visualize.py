import numpy as np
import pyqtgraph as pg  # type: ignore
from PyQt6 import QtCore, QtWidgets

pg.setConfigOptions(antialias=True)


class MainWindow(QtWidgets.QMainWindow):
    """Subclass of QMainWindow to customize application's main window"""

    def __init__(self, Ex: np.ndarray, Hy: np.ndarray) -> None:
        super().__init__()
        self.Ex: np.ndarray = Ex
        self.Hy: np.ndarray = Hy
        self.index: int = 0

        # set the size parameters (width, height) pixels
        self.setFixedSize(QtCore.QSize(640, 480))

        # set the central widget of the window
        self.graph_widget = pg.GraphicsLayoutWidget(show=True)
        self.setCentralWidget(self.graph_widget)

        # set the background color using hex notation #000000 as string
        self.graph_widget.setBackground("#000000")

        # widget for generating multi-panel figures
        self.graph_line1 = self.graph_widget.addPlot(row=0, col=0)
        self.graph_line2 = self.graph_widget.addPlot(row=1, col=0)

        # set the axis labels (position and text), style parameters
        styles = {"color": "#dcdcdc", "font-size": "10pt"}
        self.graph_line1.setLabel("left", "E<sub>x</sub>", **styles)
        self.graph_line1.setLabel("bottom", " ", **styles)
        self.graph_line2.setLabel("left", "H<sub>y</sub>", **styles)
        self.graph_line2.setLabel("bottom", "Spatial Step", **styles)

        # graph_plot method call
        self.graph_plot(self.Ex, self.Hy)

    def graph_plot(self, Ex: np.ndarray, Hy: np.ndarray) -> None:
        """Method accepts Ex and Hy parameters to plot"""

        # set the axis limits within the specified ranges and padding
        self.graph_line1.setXRange(0, Ex.shape[1], padding=0)
        self.graph_line1.setYRange(-1.2, 1.2, padding=0.1)
        self.data_line1 = self.graph_line1.plot(pen="#dcdcdc")

        # set the axis limits within the specified ranges and padding
        self.graph_line2.setXRange(0, Hy.shape[1], padding=0)
        self.graph_line2.setYRange(-1.2, 1.2, padding=0.1)
        self.data_line2 = self.graph_line2.plot(pen="#dcdcdc")

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self) -> None:
        """Method uses QTimer to update the data every 50 ms"""
        if self.index < self.Ex.shape[0]:
            self.data_line1.setData(self.Ex[self.index])
            self.data_line2.setData(self.Hy[self.index])
            self.index += 1
