from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import random
import sip

class NewTournamentWindow:
    def __init__(self):
        self.app = QApplication([])
        self.w = loadUi("newTournament.ui")
        self.w.buttonBox.accepted.connect(self.handleExitWithSave)
        self.w.buttonBox.rejected.connect(self.closeWindow)
        self.w.pushButton_addShooter.clicked.connect(self.addShooter)

        self.shooter = []
        self.enemys = []

    def run(self):
        self.w.show()
        self.app.exec()

    #reads all inforamtion and writes it to the database
    def handleExitWithSave(self):
        name = self.w.lineEdit_name.text()
        kind = self.w.comboBox_type.currentText()
        date = self.w.calendarWidget.selectedDate()
        shooters = []
        for i in self.shooter:
            shooters.append(i.itemAt(0).widget().text())
        enemys = []

        #TODO: save in database
        #print("New Entry saved!")
        self.closeWindow()

    def closeWindow(self):
        self.w.close()

    #removes one shooter from the UI
    def removeShooter(self):
        pressedButton = self.w.sender()

        layoutToRemove = next(x for x in self.shooter if x.itemAt(1).widget() is pressedButton)
        layoutToRemove.deleteLater()
        index = self.shooter.index(layoutToRemove)
        while layoutToRemove.count():
                x = layoutToRemove.takeAt(0).widget()
                x.deleteLater()
        self.shooter.remove(layoutToRemove)

    #addes one shooter to the UI
    def addShooter(self):
        layout = QHBoxLayout()
        label = QLineEdit("Schütze"+str(random.randint(0,100)))
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        layout.addWidget(label)
        #layout.addWidget(QPushButton("Bearbeiten"))
        layout.addWidget(QPushButton("Löschen"))
        layout.itemAt(1).widget().clicked.connect(self.removeShooter)
        self.shooter += [layout]
        self.w.verticalLayout_shootersInner.insertLayout(self.w.verticalLayout_shootersInner.count()-1, layout)



