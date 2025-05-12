from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QDialog


class DialogDraggable(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._drag_position = None
        self.setWindowFlag(Qt.FramelessWindowHint)  # حذف قاب پنجره

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._drag_position:
            self.move(event.globalPosition().toPoint() - self._drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._drag_position = None
