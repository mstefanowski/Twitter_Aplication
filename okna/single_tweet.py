import urllib.request

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt


class SingleTweetWidget (QtGui.QWidget):
    def __init__ (self, parent = None):
        super(SingleTweetWidget, self).__init__(parent)
        self.textQVBoxLayout = QtGui.QVBoxLayout()
        self.textUpQLabel    = QtGui.QLabel()
        self.textDownQLabel  = QtGui.QTextBrowser()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout  = QtGui.QHBoxLayout()
        self.iconQLabel      = QtGui.QLabel()
        self.iconQLabel.setAlignment(Qt.AlignTop)
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

    def setTextUp (self, text):
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        data = urllib.request.urlopen(imagePath).read()

        image = QtGui.QImage()
        image.loadFromData(data)
        self.iconQLabel.setPixmap(QtGui.QPixmap(image))

    def setTweet (self, simplified_tweet):
        self.setTextUp(simplified_tweet["imie"])
        self.setTextDown(simplified_tweet["tekst"])
        self.setIcon(simplified_tweet["avatar"])