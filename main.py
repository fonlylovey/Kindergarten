import sys
from PyQt5 import QtWidgets

from UI.Mainwindow import MainWindow;
from UI.PlotWidget import PlotWidget;

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv);
    mainWindow = MainWindow();
    mainWindow.setFixedSize(1366, 768)
    poltWidget = PlotWidget();
    mainWindow.horizontalLayout.addWidget(poltWidget);
    mainWindow.show();
    sys.exit(app.exec());