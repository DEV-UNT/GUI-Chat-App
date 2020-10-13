# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 314)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.messageEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.messageEdit.setGeometry(QtCore.QRect(1, 200, 421, 74))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.messageEdit.setFont(font)
        self.messageEdit.setObjectName("messageEdit")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 180, 421, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.receivedMessages = QtWidgets.QTextBrowser(self.centralwidget)
        self.receivedMessages.setGeometry(QtCore.QRect(1, 2, 421, 181))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.receivedMessages.setFont(font)
        self.receivedMessages.setObjectName("receivedMessages")
        self.sendBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendBtn.setGeometry(QtCore.QRect(1, 280, 421, 31))
        self.sendBtn.setObjectName("sendBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.nickname = ""
        self.port = 8080
        self.hostname = "127.0.0.1"

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Client"))
        self.sendBtn.setText(_translate("MainWindow", "Send"))