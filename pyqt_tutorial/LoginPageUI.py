# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginPageUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginProfile(object):
    def setupUi(self, LoginProfile):
        LoginProfile.setObjectName("LoginProfile")
        LoginProfile.resize(408, 231)
        self.login_button = QtWidgets.QPushButton(LoginProfile)
        self.login_button.setGeometry(QtCore.QRect(270, 110, 75, 23))
        self.login_button.setAutoDefault(True)
        self.login_button.setObjectName("login_button")
        self.password = QtWidgets.QLabel(LoginProfile)
        self.password.setGeometry(QtCore.QRect(60, 110, 47, 12))
        self.password.setObjectName("password")
        self.account = QtWidgets.QLabel(LoginProfile)
        self.account.setGeometry(QtCore.QRect(60, 60, 91, 21))
        self.account.setObjectName("account")
        self.input_account = QtWidgets.QLineEdit(LoginProfile)
        self.input_account.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.input_account.setObjectName("input_account")
        self.input_password = QtWidgets.QLineEdit(LoginProfile)
        self.input_password.setGeometry(QtCore.QRect(130, 110, 113, 20))
        self.input_password.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.result = QtWidgets.QLabel(LoginProfile)
        self.result.setGeometry(QtCore.QRect(300, 70, 47, 12))
        self.result.setText("")
        self.result.setObjectName("result")

        self.retranslateUi(LoginProfile)
        QtCore.QMetaObject.connectSlotsByName(LoginProfile)

    def retranslateUi(self, LoginProfile):
        _translate = QtCore.QCoreApplication.translate
        LoginProfile.setWindowTitle(_translate("LoginProfile", "Login Profile"))
        self.login_button.setText(_translate("LoginProfile", "Login"))
        self.password.setText(_translate("LoginProfile", "Password"))
        self.account.setText(_translate("LoginProfile", "Account"))
        self.input_password.setPlaceholderText(_translate("LoginProfile", "密碼不超過15位，只能有數字或字母"))

