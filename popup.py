# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_UI_MainWindow(object):
    def setupUi(self, UI_MainWindow):
        UI_MainWindow.setObjectName("UI_MainWindow")
        UI_MainWindow.resize(957, 663)
        self.centralwidget = QtWidgets.QWidget(UI_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 170, 561, 241))
        self.pushButton.setObjectName("pushButton")
        UI_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UI_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 957, 32))
        self.menubar.setObjectName("menubar")
        UI_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UI_MainWindow)
        self.statusbar.setObjectName("statusbar")
        UI_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UI_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(UI_MainWindow)

        self.pushButton.clicked.connect(self.show_popup)

    def retranslateUi(self, UI_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        UI_MainWindow.setWindowTitle(_translate("UI_MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("UI_MainWindow", "Press Me"))

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Tutorial on PyQt5")
        msg.setText("this is the main text")

        # icons in popup menu
        # msg.setIcon(QMessageBox.Critical) # for showing error message
        # msg.setIcon(QMessageBox.Warning) # for showing warning message
        # msg.setIcon(QMessageBox.Information) # for showing information
        msg.setIcon(QMessageBox.Question) # for showing question type messages

        # set buttons
        # QMessageBox.Ok
        # QMessageBox.Open
        # QMessageBox.Cancel
        # QMessageBox.Close
        # QMessageBox.Yes
        # QMessageBox.No
        # QMessageBox.Retry
        # QMessageBox.Abort 
        # QMessageBox.Ignore
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok) # setting default button
        msg.setInformativeText("Information")

        msg.buttonClicked.connect(self.show_popup_btn)

        msg.setDetailedText("Hello") # creates another button on the popup which would show more details/text/info when clicked on it

        x = msg.exec_() # this is what shows the message box

    def show_popup_btn(self, i):
        print(i.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UI_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_UI_MainWindow()
    ui.setupUi(UI_MainWindow)
    UI_MainWindow.show()
    sys.exit(app.exec_())

