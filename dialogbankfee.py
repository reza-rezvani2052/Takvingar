from PySide6.QtWidgets import QDialog
from UI.ui_dialogbankfee import Ui_DialogBankFee


class DialogBankFee(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogBankFee()
        self.ui.setupUi(self)

        self.sizeHint()
