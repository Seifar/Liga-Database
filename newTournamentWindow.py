from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import newTournamentDBHandler
import GLOBAL

class NewTournamentWindow:
    def __init__(self):
        self.app = QApplication([])
        self.w = loadUi("newTournament.ui")
        self.w.buttonBox.accepted.connect(self.handleExitWithSave)
        self.w.buttonBox.rejected.connect(self.closeWindow)
        self.w.pushButton_addShooter.clicked.connect(self.addShooter)
        self.w.pushButton_addEnemy.clicked.connect(self.addEnemy)

        self.shooter = []
        self.enemies = []

    def run(self):
        self.w.show()
        self.app.exec()

    #reads all inforamtion and writes it to the database
    def handleExitWithSave(self):
        name = self.w.lineEdit_name.text()
        kind = self.w.comboBox_type.currentText()
        bow = self.w.comboBox_bow.currentText()
        date = self.w.calendarWidget.selectedDate()
        shooters = []
        for i in self.shooter:
            shooters.append(i.itemAt(0).widget().text())
        if len(shooters) < 3:
            return -1
        enemys = []
        for i in self.enemies:
            enemys.append(i.itemAt(0).widget().text())
        if len(enemys) < 3:
            return -1

        #save in database
        sqlDate = GLOBAL.QDateToSQL(date)
        sqlcommand = 'INSERT INTO {0}\n' \
                     'values (\'{1}\', \'{2}\', \'{3}\', \'{4}\')'.format(GLOBAL.TABLE_name_tournaments, name, kind, bow, sqlDate)
        GLOBAL.executeSQL(sqlcommand)

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
        label = QLineEdit("neuer Schütze")
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        layout.addWidget(label)
        layout.addWidget(QPushButton("Löschen"))
        layout.itemAt(1).widget().clicked.connect(self.removeShooter)
        self.shooter += [layout]
        self.w.verticalLayout_shootersInner.insertLayout(self.w.verticalLayout_shootersInner.count()-1, layout)

    #removes onne shooter from the UI
    def removeEnemy(self):
        pressedButton = self.w.sender()

        layoutToRemove = next(x for x in self.enemies if x.itemAt(1).widget() is pressedButton)
        layoutToRemove.deleteLater()
        index = self.enemies.index(layoutToRemove)
        while layoutToRemove.count():
            x = layoutToRemove.takeAt(0).widget()
            x.deleteLater()
        self.enemies.remove(layoutToRemove)

    #addes one enemy to the UI
    def addEnemy(self):
        layout = QHBoxLayout()
        label = QLineEdit("neuer Gegner")
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        layout.addWidget(label)
        layout.addWidget(QPushButton("Löschen"))
        layout.itemAt(1).widget().clicked.connect(self.removeEnemy)
        self.enemies += [layout]
        self.w.verticalLayout_enemysInner.insertLayout(self.w.verticalLayout_enemysInner.count() - 1, layout)
