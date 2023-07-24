from DBDialog_ui import Ui_DBDialog
from PySide6.QtWidgets import QDialog, QApplication, QLineEdit

class FormDB(QDialog, Ui_DBDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ed_pwd.setEchoMode(QLineEdit.Password)

        