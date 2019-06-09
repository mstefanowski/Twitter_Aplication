# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from okna.single_tweet import SingleTweetWidget
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

class Ui_main_window(object):
    def __init__(self, twitter):
        self.twitter = twitter

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
        self.btn_tweetnij.clicked.connect(self.write_tweets)

        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(450, 22, 201, 30))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.lista_tweetow = QtGui.QListWidget(self.centralwidget)
        self.lista_tweetow.setGeometry(QtCore.QRect(200, 72, 400, 530))
        self.lista_tweetow.setObjectName(_fromUtf8("lista_tweetow"))

        self.lista_trendow = QtGui.QListView(self.centralwidget)
        self.lista_trendow.setGeometry(QtCore.QRect(25, 150, 150, 200))
        self.lista_trendow.setObjectName(_fromUtf8("lista_trendow"))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 110, 118, 17))
        self.label.setObjectName(_fromUtf8("label"))

        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        self.load_tweets()

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("main_window", "Twitter Application", None))
        self.btn_mainWindow.setText(_translate("main_window", "Strona głowna", None))
        self.btn_powiadomienia.setText(_translate("main_window", "Powiadomienia", None))
        self.btn_tweetnij.setText(_translate("main_window", "Tweetnij", None))
        self.lineEdit.setText(_translate("main_window", "Szukaj", None))
        self.label.setText(_translate("main_window", "Trendy dla Ciebie", None))

    def load_tweets(self):
        tweets = self.twitter.get_latest_tweets()
        simplified_tweets = []
        for x in range(len(tweets)):
            single_simplified_tweet = {}
            single_tweet = tweets[x]
            single_simplified_tweet["imie"] = single_tweet["user"]["name"]
            single_simplified_tweet["avatar"] = single_tweet["user"]["profile_image_url"]
            single_simplified_tweet["tekst"] = single_tweet["text"]
            simplified_tweets.append(single_simplified_tweet)
        self.set_tweets(simplified_tweets)

    def set_tweets(self, simplified_tweets):
        for i in range(len(simplified_tweets)):
            simplified_tweet = simplified_tweets[i]
            singleTweetWidget = SingleTweetWidget()
            singleTweetWidget.setTweet(simplified_tweet)
            q_list_widget_item = QtGui.QListWidgetItem(self.lista_tweetow)
            q_list_widget_item.setSizeHint(singleTweetWidget.sizeHint())
            self.lista_tweetow.addItem(q_list_widget_item)
            self.lista_tweetow.setItemWidget(q_list_widget_item, singleTweetWidget)

    def write_tweets(self):
        tweet_dialog = QtGui.QDialog()
        tweet_window = Ui_send_tweet(self.twitter)
        tweet_window.setupUi(tweet_dialog)
        tweet_dialog.exec()