from UI.ui_dialogabout import Ui_DialogAbout
from dialogdraggable import DialogDraggable


class DialogAbout(DialogDraggable):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogAbout()
        self.ui.setupUi(self)

        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        self.ui.btnOk.clicked.connect(self.accept)
