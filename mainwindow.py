from UI.ui_mainwindow import Ui_MainWindow

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QSettings


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_settings()
        # ...
        self.connect_signals_to_slots()
        # ...

    def connect_signals_to_slots(self):
        self.ui.actAbout.triggered.connect(self.actAbout_triggered)
        self.ui.actHelp.triggered.connect(self.actHelp_triggered)

        # self.ui.btnCancelProcess.clicked.connect(self.cancel_process)

    def actHelp_triggered(self):
        print("actHelp_triggered")

    def actAbout_triggered(self):
        from dialogabout import DialogAbout
        about_dialog = DialogAbout(self)
        about_dialog.exec()

    # ..........................................................................

    def closeEvent(self, event):
        self.save_settings()
        super().closeEvent(event)

    def load_settings(self):
        settings = QSettings("Takvingar", "MainWindow")
        self.restoreGeometry(settings.value("geometry", b""))
        self.restoreState(settings.value("window_state", b""))

    def save_settings(self):
        settings = QSettings("Takvingar", "MainWindow")
        settings.setValue("geometry", self.saveGeometry())
        settings.setValue("window_state", self.saveState())

    # ..........................................................................
