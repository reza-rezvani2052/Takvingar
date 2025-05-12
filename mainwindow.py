import sys
import subprocess

from UI.ui_mainwindow import Ui_MainWindow
from main import db_conn, write_app_settings

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
        self.ui.actRestartApp.triggered.connect(self.actRestartApp_triggered)

        self.ui.actAbout.triggered.connect(self.actAbout_triggered)
        self.ui.actHelp.triggered.connect(self.actHelp_triggered)

        # self.ui.btnCancelProcess.clicked.connect(self.cancel_process)

    def actQuit_triggered(self):
        self.prepare_to_close(write_settings=False)
        QApplication.quit()

    def actRestartApp_triggered(self):
        self.prepare_to_close(write_settings=False)

        # ...
        # NOTE:
        # در پای چارم، هنگام ریست برنامه، خوب همل نمیکنه اما اگر از خط فرمان
        # اجرا شود مشکلی ندارد. بعدا در انتشار نهایی برنامه این را تست کنم

        subprocess.Popen([sys.executable] + sys.argv)
        QApplication.quit()

    def actHelp_triggered(self):
        from PySide6.QtCore import QUrl
        from PySide6.QtGui import QDesktopServices

        url = QUrl.fromLocalFile("RC/help/index.html")
        QDesktopServices.openUrl(url)
        # ...
        # import webbrowser
        # webbrowser.open("https://www.google.com/")

    def actAbout_triggered(self):
        from dialogabout import DialogAbout
        about_dialog = DialogAbout(self)
        about_dialog.exec()

    # ..........................................................................

    def prepare_to_close(self, write_settings=True):
        if write_settings:
            self.save_settings()
            write_app_settings()

        if db_conn.isOpen():
            db_conn.close()

    def closeEvent(self, event):
        # اگر بعدا سیستم تری به برنامه اضافه کردم، باید مواظب باشم که در صورت
        # رفتن برنامه به سیستم تری، در فراخوانی تابع زیر کانکشن پایگاه داده بسته نشه
        self.prepare_to_close(write_settings=True)

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
