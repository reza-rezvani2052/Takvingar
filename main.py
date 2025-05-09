import os, sys
import subprocess


def convert_all_ui_files():
    ui_dir = "UI"
    for filename in os.listdir(ui_dir):
        if filename.endswith(".ui"):
            in_path = os.path.join(ui_dir, filename)
            out_name = f"ui_{os.path.splitext(filename)[0]}.py"
            out_path = os.path.join(ui_dir, out_name)
            if not os.path.exists(out_path) or os.path.getmtime(in_path) > os.path.getmtime(out_path):
                print(f"Converting: {filename} -> {out_name}")
                subprocess.run(["pyside6-uic", in_path, "-o", out_path], check=True)


convert_all_ui_files()

# بلوک کدهای فوق، حتما باید قبل از کدهای زیر باشد

# ----------------------------------------------------------------------------

import time
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QSplashScreen

from mainwindow import MainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setLayoutDirection(Qt.RightToLeft)

    # ...

    splash_image_path = os.path.join(os.path.dirname(__file__) + "/RC", 'splash.png')
    print(f"splash_image_path = {splash_image_path}")  # TODO: در انتشار نهایی این را حذف کنم
    if os.path.exists(splash_image_path):
        splash_pix = QPixmap(splash_image_path)
    else:
        splash_pix = QPixmap("./_internal/splash.png")

    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlag(Qt.FramelessWindowHint)
    splash.show()

    #  اجازه میدیم کمی سیستم پردازش کنه
    app.processEvents()

    time.sleep(1)  # TODO: ????

    # ...

    window = MainWindow()
    window.show()

    # ...

    splash.finish(window)

    # ...

    sys.exit(app.exec())
