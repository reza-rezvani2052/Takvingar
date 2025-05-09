from UI.ui_mainwindow import Ui_MainWindow

from PySide6.QtCore import QSettings

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox
)


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
        self.ui.actQuit.triggered.connect(self.actQuit_triggered)

        self.ui.actAbout.triggered.connect(self.actAbout_triggered)
        self.ui.actHelp.triggered.connect(self.actHelp_triggered)

        # self.ui.btnCancelProcess.clicked.connect(self.cancel_process)

    def actQuit_triggered(self):
        QApplication.quit()

    def actHelp_triggered(self):
        from PySide6.QtCore import QUrl
        from PySide6.QtGui import QDesktopServices

        url = QUrl.fromLocalFile("RC/help/index.html")
        QDesktopServices.openUrl(url)

    def actAbout_triggered(self):
        from dialogabout import DialogAbout
        about_dialog = DialogAbout(self)
        about_dialog.exec()

    # ..........................................................................

    def closeEvent(self, event):
        self.save_settings()
        super().closeEvent(event)
        """
        reply = QMessageBox.question(
            self, "Exit", "Are you sure you want to exit?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            # اینجا می‌تونی هر کار تمیزکاری (cleanup) انجام بدی
            event.accept()
        else:
            event.ignore()
        """

    def load_settings(self):
        settings = QSettings("Takvingar", "MainWindow")
        self.restoreGeometry(settings.value("geometry", b""))
        self.restoreState(settings.value("window_state", b""))

    def save_settings(self):
        settings = QSettings("Takvingar", "MainWindow")
        settings.setValue("geometry", self.saveGeometry())
        settings.setValue("window_state", self.saveState())

    # ..........................................................................
