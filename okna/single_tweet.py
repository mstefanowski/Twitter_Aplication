# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'single_tweet.ui'
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

class Ui_single_tweet(object):
    def setupUi(self, parent):
        parent.setObjectName(_fromUtf8("parent"))
        parent.resize(400, 186)
        parent.setMinimumSize(QtCore.QSize(400, 0))
        parent.setMaximumSize(QtCore.QSize(400, 16777215))
        self.tresc_tweeta = QtGui.QTextBrowser(parent)
        self.tresc_tweeta.setGeometry(QtCore.QRect(15, 70, 371, 101))
        self.tresc_tweeta.setObjectName(_fromUtf8("tresc_tweeta"))
        self.nazwa_uzytkownika = QtGui.QLabel(parent)
        self.nazwa_uzytkownika.setGeometry(QtCore.QRect(80, 20, 66, 17))
        self.nazwa_uzytkownika.setObjectName(_fromUtf8("nazwa_uzytkownika"))
        self.zdjecie = QtGui.QGraphicsView(parent)
        self.zdjecie.setGeometry(QtCore.QRect(20, 10, 41, 41))
        self.zdjecie.setObjectName(_fromUtf8("zdjecie"))

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)

    def retranslateUi(self, parent):
        parent.setWindowTitle(_translate("parent", "Form", None))
        self.nazwa_uzytkownika.setText(_translate("parent", "TextLabel", None))

