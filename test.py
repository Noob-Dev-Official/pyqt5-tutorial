# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Test") # i think this is like JFrame
        MainWindow.resize(904, 624)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow) # i think this is like JPanel
        self.centralwidget.setObjectName("centralwidget")
        
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(380, 410, 99, 30))
        self.button1.setObjectName("button1")
        
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(400, 150, 81, 22))
        self.label1.setObjectName("label1")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 904, 32))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # trigger is an event listener which means like onClick or clicked or something, trigger also listens for shortcut keys so when they are used, this will trigger the event
        # lambda was used so that we can pass params to the clicked function, without it, it is impossibel to pass one
        self.actionNew.triggered.connect(lambda: self.clicked("new was clicked"))
        self.actionSave.triggered.connect(lambda: self.clicked("save was clicked"))
        self.actionCopy.triggered.connect(lambda: self.clicked("copy was clicked"))
        self.actionPaste.triggered.connect(lambda: self.clicked("paste was clicked"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        self.button1.setText(_translate("MainWindow", "Press me"))
        
        self.label1.setText(_translate("MainWindow", "Its a Label"))
        
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save the file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Copy a file"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste a file"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        
    def clicked(self, text):
        self.label1.setText(text)
        self.label1.adjustSize()
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

