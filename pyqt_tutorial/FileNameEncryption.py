# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileNameEncryption.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FileEncryption(object):
    def setupUi(self, FileEncryption):
        FileEncryption.setObjectName("FileEncryption")
        FileEncryption.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(FileEncryption)
        self.centralwidget.setObjectName("centralwidget")
        self.input_file_address = QtWidgets.QLineEdit(self.centralwidget)
        self.input_file_address.setGeometry(QtCore.QRect(120, 70, 171, 20))
        self.input_file_address.setObjectName("input_file_address")
        self.input_file_name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_file_name.setGeometry(QtCore.QRect(120, 120, 171, 20))
        self.input_file_name.setObjectName("input_file_name")
        self.file_address = QtWidgets.QLabel(self.centralwidget)
        self.file_address.setGeometry(QtCore.QRect(40, 72, 71, 20))
        self.file_address.setObjectName("file_address")
        self.file_name = QtWidgets.QLabel(self.centralwidget)
        self.file_name.setGeometry(QtCore.QRect(50, 120, 61, 20))
        self.file_name.setObjectName("file_name")
        self.sequence = QtWidgets.QLabel(self.centralwidget)
        self.sequence.setGeometry(QtCore.QRect(50, 170, 61, 16))
        self.sequence.setObjectName("sequence")
        self.input_sequence = QtWidgets.QLineEdit(self.centralwidget)
        self.input_sequence.setGeometry(QtCore.QRect(120, 170, 171, 20))
        self.input_sequence.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.input_sequence.setObjectName("input_sequence")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(340, 170, 75, 23))
        self.start_button.setObjectName("start_button")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(120, 210, 301, 16))
        self.result.setText("")
        self.result.setObjectName("result")
        FileEncryption.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FileEncryption)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        FileEncryption.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FileEncryption)
        self.statusbar.setObjectName("statusbar")
        FileEncryption.setStatusBar(self.statusbar)
        self.actionAbout_Filename_Encryption = QtWidgets.QAction(FileEncryption)
        self.actionAbout_Filename_Encryption.setObjectName("actionAbout_Filename_Encryption")
        self.menuHelp.addAction(self.actionAbout_Filename_Encryption)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(FileEncryption)
        QtCore.QMetaObject.connectSlotsByName(FileEncryption)

    def retranslateUi(self, FileEncryption):
        _translate = QtCore.QCoreApplication.translate
        FileEncryption.setWindowTitle(_translate("FileEncryption", "File Encryption"))
        self.file_address.setText(_translate("FileEncryption", "File Address"))
        self.file_name.setText(_translate("FileEncryption", "File Name"))
        self.sequence.setText(_translate("FileEncryption", "Sequence"))
        self.input_sequence.setText(_translate("FileEncryption", "1"))
        self.input_sequence.setPlaceholderText(_translate("FileEncryption", "input 1 to start from 1"))
        self.start_button.setText(_translate("FileEncryption", "Start"))
        self.menuHelp.setTitle(_translate("FileEncryption", "Help"))
        self.actionAbout_Filename_Encryption.setText(_translate("FileEncryption", "About Filename Encryption"))

