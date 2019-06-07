from Twitter import Twitter_client
from PyQt4 import QtGui
import sys
from okna.login_widget import Ui_Logowanie
from okna.main_window import Ui_main_window

twitter = Twitter_client()


def run():
    app = QtGui.QApplication(sys.argv)

    login_dialog = QtGui.QDialog()
    login_Window = Ui_Logowanie(twitter)
    login_Window.setupUi(login_dialog)
    login_dialog.exec()

    if(login_Window.loged):
        window = QtGui.QMainWindow()
        main_window = Ui_main_window(twitter)
        main_window.setupUi(window)
        window.show()
        sys.exit(app.exec())

run()