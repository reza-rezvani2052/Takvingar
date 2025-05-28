from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QTimer

from UI.ui_dialogpopup import Ui_DialogPopup


class DialogPopup(QWidget):
    def __init__(self, message, duration=3000, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogPopup()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup | Qt.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.lblMessage.setText(message)

        self.adjustSize()

        if parent:
            parent_geometry = parent.geometry()
            self.move(
                    parent_geometry.x() + (parent_geometry.width() - self.width()) // 2,
                    parent_geometry.y() + (parent_geometry.height() - self.height()) // 2
                    )

        # تایمر برای بستن خودکار
        if duration > 0:
            QTimer.singleShot(duration, self.close)
