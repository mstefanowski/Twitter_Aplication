from Twitter import Twitter_client
from PyQt4 import QtGui
import sys
from okna.login_widget import Ui_Logowanie

twitter = Twitter_client()

twitter.login()
print(twitter.get_user_data())
print(twitter.get_latest_tweets())

def run():
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    Login_Window = Ui_Logowanie()
    Login_Window.setupUi(window)
    window.show()
    sys.exit(app.exec())

run()