# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.first = QtWidgets.QLineEdit(self.centralwidget)
        self.first.setGeometry(QtCore.QRect(120, 130, 113, 21))
        self.first.setObjectName("first")
        self.operations = QtWidgets.QComboBox(self.centralwidget)
        self.operations.setGeometry(QtCore.QRect(350, 130, 104, 26))
        self.operations.setObjectName("operations")
        self.second = QtWidgets.QLineEdit(self.centralwidget)
        self.second.setGeometry(QtCore.QRect(590, 130, 113, 21))
        self.second.setObjectName("second")
        self.calcbtn = QtWidgets.QPushButton(self.centralwidget)
        self.calcbtn.setGeometry(QtCore.QRect(350, 200, 113, 32))
        self.calcbtn.setObjectName("calcbtn")
        self.answer = QtWidgets.QLineEdit(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(350, 270, 113, 21))
        self.answer.setObjectName("answer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.calcbtn.clicked.connect(MainWindow.oncalculate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calcbtn.setText(_translate("MainWindow", "Calculate"))

