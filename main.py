from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from screens.avaliation_screen import Ui_Avaliation
import utils, sys

def start_system():
    # print("Olá, Seja bem vindo ao MetricsManager!")
    # comment = input("Digite seu comentário de avaliação: ")
    # clasification = utils.classify(comment)
    
    # try:
    #     utils.insert_in_file(clasification, comment)
    # except Exception as err:
    #     raise Exception(f"Ocorreu um erro ao inserir no arquivo! {err}")
    ...

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_wnd = QtWidgets.QMainWindow()
    ui = Ui_Avaliation()
    ui.setupUi(main_wnd)
    main_wnd.show()
    sys.exit(app.exec_())