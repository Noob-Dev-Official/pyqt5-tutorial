# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImageSelector(object):
    def setupUi(self, ImageSelector):
        ImageSelector.setObjectName("ImageSelector")
        ImageSelector.resize(950, 699)
        
        self.centralwidget = QtWidgets.QWidget(ImageSelector)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 140, 471, 271))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/f1.jpeg"))
        
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        
        self.mercedesBtn = QtWidgets.QPushButton(self.centralwidget)
        self.mercedesBtn.setGeometry(QtCore.QRect(140, 540, 99, 30))
        self.mercedesBtn.setObjectName("mercedesBtn")
        
        self.redbullBtn = QtWidgets.QPushButton(self.centralwidget)
        self.redbullBtn.setGeometry(QtCore.QRect(690, 540, 99, 30))
        self.redbullBtn.setObjectName("redbullBtn")
        
        self.formulaLabel = QtWidgets.QLabel(self.centralwidget)
        self.formulaLabel.setGeometry(QtCore.QRect(440, 50, 71, 22))
        self.formulaLabel.setStyleSheet("color: rgb(170, 0, 0);")
        self.formulaLabel.setScaledContents(False)
        self.formulaLabel.setObjectName("formulaLabel")
        
        ImageSelector.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(ImageSelector)
        self.statusbar.setObjectName("statusbar")
        
        ImageSelector.setStatusBar(self.statusbar)

        self.retranslateUi(ImageSelector)
        QtCore.QMetaObject.connectSlotsByName(ImageSelector)
        
        # action listeners
        self.mercedesBtn.clicked.connect(self.set_mercedes)
        self.redbullBtn.clicked.connect(self.set_redbull)

    def retranslateUi(self, ImageSelector):
        _translate = QtCore.QCoreApplication.translate
        ImageSelector.setWindowTitle(_translate("ImageSelector", "MainWindow"))
        self.mercedesBtn.setText(_translate("ImageSelector", "Mercedes"))
        self.redbullBtn.setText(_translate("ImageSelector", "Redbull"))
        self.formulaLabel.setText(_translate("ImageSelector", "Formula 1"))
        
    def set_mercedes(self):
        self.label.setPixmap(QtGui.QPixmap("img/f1_mercedes.jpeg"))
        
    def set_redbull(self):
        self.label.setPixmap(QtGui.QPixmap("img/f1_redbull.jpeg"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImageSelector = QtWidgets.QMainWindow()
    ui = Ui_ImageSelector()
    ui.setupUi(ImageSelector)
    ImageSelector.show()
    sys.exit(app.exec_())

