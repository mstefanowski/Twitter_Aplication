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
    def setupUi(self, Logowanie):
        Logowanie.setObjectName(_fromUtf8("Logowanie"))
        Logowanie.resize(400, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Logowanie.sizePolicy().hasHeightForWidth())
        Logowanie.setSizePolicy(sizePolicy)
        Logowanie.setMinimumSize(QtCore.QSize(400, 300))
        Logowanie.setMaximumSize(QtCore.QSize(400, 300))
        self.login_browser = QtGui.QTextBrowser(Logowanie)
        self.login_browser.setGeometry(QtCore.QRect(150, 70, 221, 41))
        self.login_browser.setObjectName(_fromUtf8("login_browser"))
        self.password_browser = QtGui.QTextBrowser(Logowanie)
        self.password_browser.setGeometry(QtCore.QRect(150, 130, 221, 41))
        self.password_browser.setObjectName(_fromUtf8("password_browser"))
        self.main_label = QtGui.QLabel(Logowanie)
        self.main_label.setGeometry(QtCore.QRect(160, 20, 71, 17))
        self.main_label.setObjectName(_fromUtf8("main_label"))
        self.btn_logIn = QtGui.QPushButton(Logowanie)
        self.btn_logIn.setGeometry(QtCore.QRect(246, 216, 121, 51))
        self.btn_logIn.setObjectName(_fromUtf8("btn_logIn"))
        self.login_label = QtGui.QLabel(Logowanie)
        self.login_label.setGeometry(QtCore.QRect(50, 80, 66, 17))
        self.login_label.setObjectName(_fromUtf8("login_label"))
        self.password_label = QtGui.QLabel(Logowanie)
        self.password_label.setGeometry(QtCore.QRect(50, 140, 66, 17))
        self.password_label.setObjectName(_fromUtf8("password_label"))

        self.retranslateUi(Logowanie)
        QtCore.QMetaObject.connectSlotsByName(Logowanie)

    def retranslateUi(self, Logowanie):
        Logowanie.setWindowTitle(_translate("Logowanie", "Form", None))
        self.main_label.setText(_translate("Logowanie", "Zaloguj się", None))
        self.btn_logIn.setText(_translate("Logowanie", "Zaloguj się", None))
        self.login_label.setText(_translate("Logowanie", "Login", None))
        self.password_label.setText(_translate("Logowanie", "Hasło", None))
