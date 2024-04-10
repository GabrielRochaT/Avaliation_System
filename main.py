from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from screens.main_menu import Ui_Menu
import utils, sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_wnd = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(main_wnd)
    main_wnd.show()
    sys.exit(app.exec_())