# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_widget.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Logowanie(object):

    def __init__(self, twitter):
        self.twitter = twitter

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Logowanie"))
        MainWindow.resize(400, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setMaximumSize(QtCore.QSize(400, 300))
        self.login_field = QtGui.QLineEdit(MainWindow)
        self.login_field.setGeometry(QtCore.QRect(150, 70, 221, 41))
        self.login_field.setObjectName(_fromUtf8("login_browser"))
        self.password_field = QtGui.QLineEdit(MainWindow)
        self.password_field.setGeometry(QtCore.QRect(150, 130, 221, 41))
        self.password_field.setObjectName(_fromUtf8("password_browser"))
        self.main_label = QtGui.QLabel(MainWindow)
        self.main_label.setGeometry(QtCore.QRect(160, 20, 71, 17))
        self.main_label.setObjectName(_fromUtf8("main_label"))
        self.btn_logIn = QtGui.QPushButton(MainWindow)
        self.btn_logIn.setGeometry(QtCore.QRect(246, 216, 121, 51))
        self.btn_logIn.setObjectName(_fromUtf8("btn_logIn"))
        self.btn_logIn.clicked.connect(self.login_clicked)
        self.login_label = QtGui.QLabel(MainWindow)
        self.login_label.setGeometry(QtCore.QRect(50, 80, 66, 17))
        self.login_label.setObjectName(_fromUtf8("login_label"))
        self.password_label = QtGui.QLabel(MainWindow)
        self.password_label.setGeometry(QtCore.QRect(50, 140, 66, 17))
        self.password_label.setObjectName(_fromUtf8("password_label"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Logowanie", "Zaloguj się", None))
        self.main_label.setText(_translate("Logowanie", "Zaloguj się", None))
        self.btn_logIn.setText(_translate("Logowanie", "Zaloguj się", None))
        self.login_label.setText(_translate("Logowanie", "Login", None))
        self.password_label.setText(_translate("Logowanie", "Hasło", None))

    def login_clicked(self):
        self.twitter.login()
        print(self.twitter.get_user_data())
        print(self.twitter.get_latest_tweets())