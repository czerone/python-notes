# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginPageUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(408, 231)
        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(270, 110, 75, 23))
        self.login.setObjectName("login")
        self.password = QtWidgets.QLabel(Form)
        self.password.setGeometry(QtCore.QRect(60, 110, 47, 12))
        self.password.setObjectName("password")
        self.account = QtWidgets.QLabel(Form)
        self.account.setGeometry(QtCore.QRect(60, 60, 91, 21))
        self.account.setObjectName("account")
        self.input_account = QtWidgets.QLineEdit(Form)
        self.input_account.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.input_account.setObjectName("input_account")
        self.input_password = QtWidgets.QLineEdit(Form)
        self.input_password.setGeometry(QtCore.QRect(130, 110, 113, 20))
        self.input_password.setObjectName("input_password")
        self.result = QtWidgets.QLabel(Form)
        self.result.setGeometry(QtCore.QRect(300, 70, 47, 12))
        self.result.setText("")
        self.result.setObjectName("result")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.login.setText(_translate("Form", "Login"))
        self.password.setText(_translate("Form", "Password"))
        self.account.setText(_translate("Form", "Account"))

