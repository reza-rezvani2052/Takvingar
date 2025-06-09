import os
import sys
import shutil
import logging
import subprocess

import time
from datetime import datetime, timedelta
import jdatetime  # تاریخ شمسی

from PySide6.QtCore import QSettings, QTimer
from PySide6.QtGui import QIcon, QMovie, Qt
from PySide6.QtWidgets import (QApplication, QDialog, QFileDialog, QLabel, QMainWindow, QMessageBox, QVBoxLayout)

# اگر دسترسی خواندنی و نوشتنی به متغیرهای سراسری  بخواهیم
# باید دستور ایمپورت را به صورت زیر بنویسیم
# اگر از from استفاده کنیم، فقط دسترسی خواندنی داریم
import DB.database
import DB.settings

from definitions import app_info, app_settings, user_info
from dialogpopup import DialogPopup
from dialogdraggable import DialogDraggable

from main import write_app_settings
from UI.ui_mainwindow import Ui_MainWindow

# NOTE: این پوشه در کنار فایل اجرایی برنامه به صورت خودکار ساخته میشود
BACKUP_FOLDER = "backups"
MAX_BACKUPS = 5


######################################################################################################

class BackupProgressDialog(DialogDraggable):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowTitle("در حال پشتیبان‌گیری")
        self.setModal(True)
        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        # self.setFixedSize(250, 100)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(25, 25, 25, 25)
        self.label = QLabel("⏳ در حال پشتیبان گیری. لطفاً منتظر بمانید...", self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.spinner = QLabel(self)
        self.spinner.setAlignment(Qt.AlignCenter)
        movie = QMovie(":/img/spinner.gif")
        self.spinner.setMovie(movie)
        movie.start()
        layout.addWidget(self.spinner)
        self.sizeHint()


######################################################################################################

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.toolBar.setWindowTitle("نوار ابزار")
        self.read_settings()
        # ...
        self.connect_signals_to_slots()
        # ...
        self.last_backup_time = datetime.min  # زمان آخرین بکاپ
        self.data_modified_since_backup = False  # آیا داده‌ای از آخرین بکاپ تغییر کرده؟

        self.check_user_access_level()
        self.warmup_dialogs()

        self.setup_auto_backup_timer()

        # TODO: وقتی داده‌ای تغییر می‌کند
        # self.data_modified_since_backup = True
        # ...

    def connect_signals_to_slots(self):
        self.ui.actQuit.triggered.connect(self.actQuit_triggered)
        self.ui.actRestartApp.triggered.connect(self.actRestartApp_triggered)

        self.ui.actBackup.triggered.connect(self.actBackup_triggered)
        self.ui.actRestoreBackup.triggered.connect(self.actRestoreBackup_triggered)

        self.ui.actExportDataToExcel.triggered.connect(self.actExportDataToExcel_triggered)
        self.ui.actImportDataFromExcel.triggered.connect(self.actImportDataFromExcel_triggered)

        self.ui.actBankFeeCalculator.triggered.connect(self.actBankFeeCalculator_triggered)

        self.ui.actHelp.triggered.connect(self.actHelp_triggered)
        self.ui.actAbout.triggered.connect(self.actAbout_triggered)

    def check_user_access_level(self):
        username_fa = ""
        if user_info.access_level < 1:  # Limited user
            # TODO: * Disable some features & menus

            self.ui.actBackup.setEnabled(False)
            self.ui.actRestoreBackup.setEnabled(False)

            self.ui.actExportDataToExcel.setEnabled(False)
            self.ui.actImportDataFromExcel.setEnabled(False)

            # self.ui.mnuManagement.setEnabled(False)
            for action in self.ui.mnuManagement.actions():
                action.setEnabled(False)

            # self.ui.mnuTools.setEnabled(False)
            for action in self.ui.mnuTools.actions():
                action.setEnabled(False)

            self.ui.statusbar.showMessage(user_info.username)
            username_fa = f"({user_info.username})کاربر محدود"
        else:
            username_fa = f"({user_info.username})مدیر سیستم"

        self.ui.statusbar.showMessage(username_fa)

    def warmup_dialogs(self):
        # NOTE: در اینجا وارم آپ انجام بشه
        dummy = BackupProgressDialog(self)
        dummy.close()
        dummy.deleteLater()

    def create_db_backup(self, show_message=True, auto_backup=False) -> tuple[bool, str]:
        try:
            # ایجاد نام پیش‌فرض با تاریخ و زمان جاری به شمسی
            now_gregorian = datetime.now()
            now_jalali = jdatetime.datetime.fromgregorian(datetime=now_gregorian)
            default_name = f"backup_{now_jalali.strftime('%Y-%m-%d_%H-%M-%S')}.db"

            # بررسی وجود فایل مبدا
            source_path = DB.database.Connections['CONN_DATA']['PATH']
            if not os.path.exists(source_path):
                err_msg = f"فایل پایگاه داده یافت نشد:\n{source_path}"
                if show_message:
                    QMessageBox.critical(self, "خطا", err_msg)
                return False, err_msg

            # گرفتن مسیر ذخیره‌سازی از کاربر
            # اگر بکاپ بصورت سیستمی و خودکار است نیازی به بازشدن دیالوگ زیر نیست
            if auto_backup:
                show_message = False
                os.makedirs(BACKUP_FOLDER, exist_ok=True)
                dest_path = os.path.join(BACKUP_FOLDER, default_name)
            else:
                dest_path, _ = QFileDialog.getSaveFileName(
                        self, "ذخیره نسخه پشتیبان", default_name, "Database Files (*.db)"
                        )
                if not dest_path:
                    return False, "پشتیبان‌گیری لغو شد"

            if not dest_path.lower().endswith(".db"):
                dest_path += ".db"

            # ...
            dialog = None
            t_start = time.time()
            if show_message and not auto_backup:
                dialog = BackupProgressDialog(self)
                QTimer.singleShot(0, dialog.show)  # جلوگیری از فریز UI
            # ...

            shutil.copy2(source_path, dest_path)

            if auto_backup:
                # مدیریت تعداد فایل‌های پشتیبان
                backups = sorted(
                        [f for f in os.listdir(BACKUP_FOLDER) if f.endswith(".db")],
                        reverse=True  # جدیدترین ابتدا
                        )
                for old_backup in backups[MAX_BACKUPS:]:
                    try:
                        os.remove(os.path.join(BACKUP_FOLDER, old_backup))
                    except Exception as e:
                        logging.debug(f"⚠️ خطا در حذف فایل قدیمی: {old_backup} => {e}")

            # ...
            if dialog:
                elapsed = time.time() - t_start
                if elapsed < 3.0:
                    # QTimer.singleShot(int((5.0 - elapsed) * 1000), dialog.accept)
                    QTimer.singleShot(
                            int((3.0 - elapsed) * 1000),
                            lambda: self.on_backup_finished(dest_path, show_message, dialog)
                            )
                else:
                    dialog.accept()
            # ...
            _msg = "✅ نسخه پشتیبان با موفقیت ذخیره شد:\n" + dest_path
            return True, _msg

        except Exception as e:
            if dialog:
                dialog.accept()

            err_msg = f"در هنگام پشتیبان‌گیری خطایی رخ داد:\n{str(e)}"
            if show_message:
                QMessageBox.critical(self, "خطا", err_msg)
            return False, err_msg

    def on_backup_finished(self, dest_path, show_message, dialog):
        _msg = "✅ نسخه پشتیبان با موفقیت ذخیره شد:\n" + dest_path
        if dialog:
            dialog.accept()
        if show_message:
            DialogPopup(_msg, duration=4000, parent=self).show()

    def setup_auto_backup_timer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.check_and_auto_backup)
        timer.start(5 * 60 * 1000)  # بررسی هر ۵ دقیقه

    def check_and_auto_backup(self):
        # self.data_modified_since_backup = True

        now = datetime.now()
        elapsed = now - self.last_backup_time

        # بیشتر ا 30 دقیقه از آخرین بکاپ گذشته باشد
        if self.data_modified_since_backup and elapsed >= timedelta(minutes=30):
            success, _ = self.create_db_backup(auto_backup=True)
            if success:
                self.last_backup_time = now
                self.data_modified_since_backup = False
                logging.debug("Auto Backup created successfully!")

    def actBackup_triggered(self):
        self.create_db_backup(show_message=True)
        # self.create_db_backup(show_message=False, auto_backup=True)

    @staticmethod
    def are_paths_equal(path1, path2):
        abs_path1 = os.path.abspath(os.path.realpath(path1))
        abs_path2 = os.path.abspath(os.path.realpath(path2))
        return abs_path1 == abs_path2

    def actRestoreBackup_triggered(self):
        # TODO:  اول فایلهای باز و نیمه کاره چک شوند و درصورت نیاز کاربر، ذخیره گردند
        # همچنین اگر نیاز بود به کاربر هشدار دهم تا تمامی پنجره ها را یا ذخیره
        # و یا ببندد
        # ...
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("راه اندازی مجدد")
        msg_box.setText(
                "پس از بازیابی نسخه پشتیبان، برنامه بسته و دوباره اجرا خواهد شد"
                "\n" + "آیا مایل به ادامه کار هستید؟",
                )
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowIcon(QIcon(":/app-icon.jpg"))
        yes_button = msg_box.addButton("بله", QMessageBox.YesRole)
        no_button = msg_box.addButton("خیر", QMessageBox.NoRole)
        msg_box.setDefaultButton(yes_button)
        msg_box.exec()

        if msg_box.clickedButton() == yes_button:

            new_db_path = DB.database.choose_database_file()
            if not new_db_path:  # کاربر کنسل کرد
                return

            if self.are_paths_equal(
                    new_db_path, DB.database.Connections['CONN_DATA']['PATH']
                    ):
                _msg = "فایل انتخاب‌شده برای بازگردانی، همان فایل پایگاه‌داده فعلی است.\n" \
                       "لطفاً یک فایل پشتیبان دیگر انتخاب کنید."
                DialogPopup(_msg, duration=6000, parent=self).show()
                return

            # ...
            # نیاز نیست که بررسی شود اینکه فایل واقعاً دیتابیس معتبر SQLite هست یا نه
            # چون باعث پیچیدگی در تابع
            #
            # میشد. مضاف بر این بعد از اجرای مجدد برنامه، این مورد بررسی میشود
            # status, message = DB.database.is_valid_sqlite_file("CONN_DATA")
            # ...

            app_settings.db_data_path = new_db_path
            DB.database.Connections['CONN_DATA']['PATH'] = new_db_path

            self.prepare_to_close(write_settings=True)
            self.actRestartApp_triggered()
        else:
            return

    def actExportDataToExcel_triggered(self):
        # TODO:
        pass

    def actImportDataFromExcel_triggered(self):
        # TODO:
        pass

    def actQuit_triggered(self):
        self.prepare_to_close(write_settings=False)
        QApplication.quit()

    def actRestartApp_triggered(self):
        self.prepare_to_close(write_settings=False)
        # ...
        subprocess.Popen([sys.executable] + sys.argv)
        QApplication.quit()

    def actBankFeeCalculator_triggered(self):
        from dialogbankfee import DialogBankFee
        bankfee_dialog = DialogBankFee(self)
        # bankfee_dialog.exec()
        bankfee_dialog.show()

    @staticmethod
    def actHelp_triggered():
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
            self.write_settings()
            write_app_settings()

        DB.database.close_all_db_connections()

    def closeEvent(self, event):
        # اگر بعدا سیستم تری به برنامه اضافه کردم، باید مواظب باشم که در صورت
        # رفتن برنامه به سیستم تری، در فراخوانی تابع زیر کانکشن پایگاه داده بسته نشه
        self.prepare_to_close(write_settings=True)

        super().closeEvent(event)

    def read_settings(self):
        settings = QSettings(app_info.application_name_en, "MainWindow")
        self.restoreGeometry(settings.value("geometry", b""))
        self.restoreState(settings.value("window_state", b""))

    def write_settings(self):
        settings = QSettings(app_info.application_name_en, "MainWindow")
        settings.setValue("geometry", self.saveGeometry())
        settings.setValue("window_state", self.saveState())

    # ..........................................................................
