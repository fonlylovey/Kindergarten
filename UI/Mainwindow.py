from PyQt5 import QtWidgets, uic;
import sys

from UI.PlotWidget import PlotWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__();
        uic.loadUi("UI/MainWindow.ui", self);