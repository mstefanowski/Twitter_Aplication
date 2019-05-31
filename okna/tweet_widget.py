# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tweet_widget.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(700, 400)
        Form.setMinimumSize(QtCore.QSize(700, 400))
        Form.setMaximumSize(QtCore.QSize(700, 400))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 50, 700, 10))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.tweet_sth = QtGui.QLabel(Form)
        self.tweet_sth.setGeometry(QtCore.QRect(307, 20, 82, 17))
        self.tweet_sth.setObjectName(_fromUtf8("tweet_sth"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(100, 80, 581, 251))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.user_photo = QtGui.QFrame(Form)
        self.user_photo.setGeometry(QtCore.QRect(20, 80, 61, 61))
        self.user_photo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.user_photo.setFrameShadow(QtGui.QFrame.Raised)
        self.user_photo.setObjectName(_fromUtf8("user_photo"))
        self.textEdit.raise_()
        self.btn_tweetnij = QtGui.QPushButton(Form)
        self.btn_tweetnij.setGeometry(QtCore.QRect(540, 340, 141, 41))
        self.btn_tweetnij.setObjectName(_fromUtf8("btn_tweetnij"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.tweet_sth.setText(_translate("Form", "Tweetnij coś", None))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Co się dzieje?</p></body></html>", None))
        self.btn_tweetnij.setText(_translate("Form", "Tweetnij", None))

