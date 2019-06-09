# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tweet_widget.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!
import urllib.request

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

class Ui_send_tweet(object):
    def __init__(self, twitter):
        self.twitter = twitter

    def setupUi(self, parent):
        self.parent = parent
        self.parent.setObjectName(_fromUtf8("Form"))
        self.parent.resize(700, 400)
        self.parent.setMinimumSize(QtCore.QSize(700, 400))
        self.parent.setMaximumSize(QtCore.QSize(700, 400))

        self.line = QtGui.QFrame(parent)
        self.line.setGeometry(QtCore.QRect(0, 50, 700, 10))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.tweet_sth = QtGui.QLabel(parent)
        self.tweet_sth.setGeometry(QtCore.QRect(307, 20, 82, 17))
        self.tweet_sth.setObjectName(_fromUtf8("tweet_sth"))

        self.textEdit = QtGui.QTextEdit(parent)
        self.textEdit.setGeometry(QtCore.QRect(100, 80, 581, 251))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.user_photo = QtGui.QLabel(parent)
        self.user_photo.setGeometry(QtCore.QRect(20, 80, 48, 48))
        self.user_photo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.user_photo.setFrameShadow(QtGui.QFrame.Raised)
        self.user_photo.setObjectName(_fromUtf8("user_photo"))

        self.textEdit.raise_()

        self.btn_tweetnij = QtGui.QPushButton(parent)
        self.btn_tweetnij.setGeometry(QtCore.QRect(540, 340, 141, 41))
        self.btn_tweetnij.setObjectName(_fromUtf8("btn_tweetnij"))
        self.btn_tweetnij.clicked.connect(self.createATweet)

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)

        self.get_user_avatar()

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Tweetnij coś", None))
        self.tweet_sth.setText(_translate("Form", "Tweetnij coś", None))
        self.btn_tweetnij.setText(_translate("Form", "Tweetnij", None))

    def createATweet(self):
        self.twitter.create_a_tweet(self.textEdit.toPlainText())
        self.parent.hide()

    def get_user_avatar(self):
        user_data = self.twitter.get_user_data()
        avatar = user_data["profile_image_url"]
        data = urllib.request.urlopen(avatar).read()
        image = QtGui.QImage()
        image.loadFromData(data)
        self.user_photo.setPixmap(QtGui.QPixmap(image))