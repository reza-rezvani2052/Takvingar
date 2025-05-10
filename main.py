from build_ui import convert_qrc_to_py, convert_all_ui_files

convert_qrc_to_py()
convert_all_ui_files()
# کدهای فوق، حتما باید قبل از کدهای زیر باشد
# TODO: در رلیز نهایی برنامه، بع از ساخت فایل مربوطه، خطوط بالا غیر فعال شوند

# ----------------------------------------------------------------------------

import time, sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import (
    QApplication, QSplashScreen, QMessageBox, QFileDialog
)

from mainwindow import MainWindow

from DB.database import *

# ...

db_conn = None
db_path = "takvingar.db"

# ...

def choose_database_file():
    file_path, _ = QFileDialog.getOpenFileName(
        None,
        "انتخاب فایل پایگاه داده",
        ".",
        "SQLite Database Files (*.db);;All Files (*)"
    )
    return file_path


def try_connect_with_retry(initial_path):
    _db_path = initial_path

    while True:
        _db_conn = connect_to_database(_db_path)

        if _db_conn is not None:
            return _db_conn, _db_path
        # ...

        msg_box = QMessageBox()
        msg_box.setWindowTitle("خطا در یافتن پایگاه داده")
        msg_box.setText("فایل مشخص‌شده برای پایگاه داده در دسترس نیست یا معتبر نمی‌باشد.\n"
                        "آیا مایل به انتخاب فایل دیگری هستید؟")
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowIcon(QIcon(":/app-icon.jpg"))

        yes_button = msg_box.addButton("بله", QMessageBox.YesRole)
        no_button = msg_box.addButton("خیر", QMessageBox.NoRole)
        msg_box.setDefaultButton(yes_button)
        msg_box.exec()

        if msg_box.clickedButton() == yes_button :
            _db_path = choose_database_file()
            if not _db_path:
                break  # کاربر انتخاب نکرد → خروج از حلقه و پایان برنامه
        else:
            break

    return None, None


# ...

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setLayoutDirection(Qt.RightToLeft)

    # ...

    db_conn, db_path = try_connect_with_retry(db_path)
    if db_conn is None:
        app.quit()
        exit(-1)

    # ...

    splash = QSplashScreen(QPixmap(":/splash.jpg"), Qt.WindowStaysOnTopHint)
    splash.setWindowFlag(Qt.FramelessWindowHint)
    splash.show()

    #  اجازه میدیم کمی سیستم پردازش کنه
    app.processEvents()

    # ...
    time.sleep(2)  # TODO: ????
    # ...

    window = MainWindow()
    window.show()

    # ...
    splash.finish(window)
    # ...

    sys.exit(app.exec())
