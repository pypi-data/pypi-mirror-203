import sys
from PyQt5 import QtWidgets
from . ui_fijiconvertdialog import Ui_MainDialog


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainDialog = QtWidgets.QDialog()
    ui = Ui_MainDialog()
    ui.setupUi(MainDialog)
    MainDialog.show()
    sys.exit(app.exec_())
