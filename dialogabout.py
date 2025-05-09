from PySide6.QtWidgets import QDialog
from UI.ui_dialogabout import Ui_DialogAbout

class DialogAbout(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogAbout()
        self.ui.setupUi(self)

        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        self.ui.btnOk.clicked.connect(self.accept)


