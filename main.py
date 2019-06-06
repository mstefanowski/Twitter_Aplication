from Twitter import Twitter_client
from PyQt4 import QtGui
import sys
from okna.login_widget import Ui_Logowanie

twitter = Twitter_client()


def run():
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    login_Window = Ui_Logowanie(twitter)
    login_Window.setupUi(window)
    window.show()
    sys.exit(app.exec())

run()