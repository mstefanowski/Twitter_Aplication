# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_window.ui'
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

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName(_fromUtf8("main_window"))
        main_window.resize(800, 600)
        main_window.setMinimumSize(QtCore.QSize(800, 600))
        main_window.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtGui.QWidget(main_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 72, 800, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.btn_mainWindow = QtGui.QPushButton(self.centralwidget)
        self.btn_mainWindow.setGeometry(QtCore.QRect(25, 22, 101, 30))
        self.btn_mainWindow.setObjectName(_fromUtf8("btn_mainWindow"))
        self.btn_powiadomienia = QtGui.QPushButton(self.centralwidget)
        self.btn_powiadomienia.setGeometry(QtCore.QRect(135, 22, 111, 30))
        self.btn_powiadomienia.setObjectName(_fromUtf8("btn_powiadomienia"))
        self.btn_tweetnij = QtGui.QPushButton(self.centralwidget)
        self.btn_tweetnij.setGeometry(QtCore.QRect(675, 22, 97, 30))
        self.btn_tweetnij.setObjectName(_fromUtf8("btn_tweetnij"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(450, 22, 201, 30))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lista_tweetow = QtGui.QListWidget(self.centralwidget)
        self.lista_tweetow.setGeometry(QtCore.QRect(200, 72, 400, 530))
        self.lista_tweetow.setObjectName(_fromUtf8("lista_tweetow"))
        self.btn_follow = QtGui.QPushButton(self.centralwidget)
        self.btn_follow.setGeometry(QtCore.QRect(625, 100, 150, 50))
        self.btn_follow.setObjectName(_fromUtf8("btn_follow"))
        self.profile_picture = QtGui.QGraphicsView(self.centralwidget)
        self.profile_picture.setGeometry(QtCore.QRect(25, 100, 150, 150))
        self.profile_picture.setObjectName(_fromUtf8("profile_picture"))
        self.profile_name = QtGui.QTextBrowser(self.centralwidget)
        self.profile_name.setGeometry(QtCore.QRect(25, 270, 150, 30))
        self.profile_name.setObjectName(_fromUtf8("profile_name"))
        self.profile_bio = QtGui.QTextBrowser(self.centralwidget)
        self.profile_bio.setGeometry(QtCore.QRect(25, 320, 150, 150))
        self.profile_bio.setObjectName(_fromUtf8("profile_bio"))
        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("main_window", "Twitter Application", None))
        self.btn_mainWindow.setText(_translate("main_window", "Strona głowna", None))
        self.btn_powiadomienia.setText(_translate("main_window", "Powiadomienia", None))
        self.btn_tweetnij.setText(_translate("main_window", "Tweetnij", None))
        self.lineEdit.setText(_translate("main_window", "Szukaj", None))
        self.btn_follow.setText(_translate("main_window", "Obserwuj", None))
        self.profile_name.setHtml(_translate("main_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Profile name</p></body></html>", None))
        self.profile_bio.setHtml(_translate("main_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Profile bio</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

