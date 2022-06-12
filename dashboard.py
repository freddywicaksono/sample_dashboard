import sys
from PyQt5 import QtCore,QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from frmGravitasi import *
from frmPrisma import *
from frmKonversisuhu import *
from frmBMI import *

qtcreator_file  = "dashboard.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class DashboardWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.actionGravitasi.triggered.connect(self.Gravitasi)
        self.actionPrisma.triggered.connect(self.Prisma)
        self.actionSuhu.triggered.connect(self.Suhu)
        self.actionBMI.triggered.connect(self.BMI)

    def Gravitasi(self):
        winGra.setWindowModality(QtCore.Qt.ApplicationModal)
        winGra.show()

    def Prisma(self):
        winPrs.setWindowModality(QtCore.Qt.ApplicationModal)
        winPrs.show()

    def Suhu(self):
        winSuhu.setWindowModality(QtCore.Qt.ApplicationModal)
        winSuhu.show()

    def BMI(self):
        winBMI.setWindowModality(QtCore.Qt.ApplicationModal)
        winBMI.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DashboardWindow()
    winGra = GravitasiWindow()
    winPrs = PrismaWindow()
    winSuhu = KonversisuhuWindow()
    winBMI = BMIWindow()
    window.show()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = DashboardWindow()