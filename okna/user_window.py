# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_window.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!
import urllib.request

from PyQt4 import QtCore, QtGui

from okna.tweet_widget import Ui_send_tweet

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

class Ui_user_window(object):
    def __init__(self, twitter):
        self.twitter = twitter

    def setupUi(self, parent):
        parent.setObjectName(_fromUtf8("main_window"))
        parent.resize(800, 600)
        parent.setMinimumSize(QtCore.QSize(800, 600))
        parent.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = parent
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
        self.btn_tweetnij.clicked.connect(self.write_tweets)

        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(450, 22, 201, 30))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.lista_tweetow = QtGui.QListWidget(self.centralwidget)
        self.lista_tweetow.setGeometry(QtCore.QRect(200, 72, 400, 530))
        self.lista_tweetow.setObjectName(_fromUtf8("lista_tweetow"))

        self.btn_follow = QtGui.QPushButton(self.centralwidget)
        self.btn_follow.setGeometry(QtCore.QRect(625, 100, 150, 50))
        self.btn_follow.setObjectName(_fromUtf8("btn_follow"))

        self.profile_photo = QtGui.QLabel(self.centralwidget)
        self.profile_photo.setGeometry(QtCore.QRect(25, 100, 150, 150))
        self.profile_photo.setObjectName(_fromUtf8("profile_picture"))

        self.profile_name = QtGui.QTextBrowser(self.centralwidget)
        self.profile_name.setGeometry(QtCore.QRect(25, 270, 150, 70))
        self.profile_name.setObjectName(_fromUtf8("profile_name"))

        self.profile_bio = QtGui.QTextBrowser(self.centralwidget)
        self.profile_bio.setGeometry(QtCore.QRect(25, 360, 150, 150))
        self.profile_bio.setObjectName(_fromUtf8("profile_bio"))

        self.retranslateUi(parent)
        QtCore.QMetaObject.connectSlotsByName(parent)
        self.get_user_avatar()
        self.get_info()

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("main_window", "Twitter Application", None))
        self.btn_mainWindow.setText(_translate("main_window", "Strona głowna", None))
        self.btn_powiadomienia.setText(_translate("main_window", "Powiadomienia", None))
        self.btn_tweetnij.setText(_translate("main_window", "Tweetnij", None))
        self.lineEdit.setText(_translate("main_window", "Szukaj", None))
        self.btn_follow.setText(_translate("main_window", "Obserwuj", None))

    def write_tweets(self):
        tweet_dialog = QtGui.QDialog()
        tweet_window = Ui_send_tweet(self.twitter)
        tweet_window.setupUi(tweet_dialog)
        tweet_dialog.exec()

    def get_user_avatar(self):
        user_data = self.twitter.get_user_data()
        avatar = user_data["profile_image_url"]
        avatar = avatar.replace("_normal", '')
        data = urllib.request.urlopen(avatar).read()
        image = QtGui.QImage()
        image.loadFromData(data)
        image = image.scaledToHeight(150)
        self.profile_photo.setPixmap(QtGui.QPixmap(image))

    def get_info(self):
        user_data = self.twitter.get_user_data()
        nick = user_data["screen_name"]
        imie = user_data["name"]
        bio = user_data["description"]
        self.profile_name.setPlainText("@"+nick+"\n"+imie)
        self.profile_bio.setPlainText(bio)
