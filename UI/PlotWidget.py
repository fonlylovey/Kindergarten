from PyQt5 import QtWidgets, QtGui;
from PyQt5.QtCore import QPoint, Qt;
from PyQt5.QtGui import *;

class PlotWidget(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self);
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine));

        points = QPolygon([
            QPoint(0, 0),
            QPoint(164, 358),
            QPoint(396, 812),
            QPoint(899, 782),
            QPoint(601, 315),
        ]);

        painter.drawPolygon(points);