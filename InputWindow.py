from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *

class InputWindow:
    def __init__(self):
        self.app = QApplication([])
        self.w = loadUi("input.ui")
        self.w.comboBox_schuetze1.addItem("Test")

    def run(self):
        self.w.show()
        self.app.exec()

