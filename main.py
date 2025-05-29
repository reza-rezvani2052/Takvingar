def build_ui_and_convert_qrc_to_py():
    from build_ui import convert_qrc_to_py, convert_all_ui_files

    convert_qrc_to_py()
    convert_all_ui_files()


# TODO: در رلیز نهایی برنامه، بعد از ساخت فایل مربوطه، خط زیر غیر فعال شود
build_ui_and_convert_qrc_to_py()

# NOTE: خطوط بالا حتما باید قبل از سایر دستورات زیر باشند
# به هشدارهای PEP که PyCharm میده توجه نکن
# چون در فایل هایی مثل DialogLogin به Resource ها نیاز داریم، بنابراین اول باید ساخته شوند
# اما در رلیز نهایی قضیه فرق میکند

# ----------------------------------------------------------------------------

import sys
import time

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QSplashScreen, QMessageBox)

from dialoglogin import DialogLogin

# import definitions
from definitions import *

# اگر دسترسی خواندنی و نوشتنی به متغیرهای سراسری  بخواهیم
# باید دستور ایمپورت را به صورت زیر بنویسیم
# اگر از from استفاده کنیم، فقط دسترسی خواندنی داریم
import DB.database
import DB.settings


# ----------------------------------------------------------------------------


def has_login_form_shown_before_and_registered() -> bool:
    options_keys = \
        [
            "HasLoginFormShownBefore",
            "IsUserRegisteredSuccessfully"
            # "NonExistentKey"
            ]

    # واکشی تنظیمات
    settings = DB.settings.get_settings_by_keys(options_keys)

    # دریافت مقادیر به صورت امن
    has_shown_before = bool(int(settings.get("HasLoginFormShownBefore", 0)))
    is_user_registered_successfully = bool(int(settings.get("IsUserRegisteredSuccessfully", 0)))
    # print(f"has_shown_before = {has_shown_before} - is_user_registered_successfully = {is_user_registered_successfully}")

    # نمایش برای تست (اختیاری)
    # for key in options_keys:
    #     print(f"{key} => {settings.get(key, 'Default Value')}")

    return has_shown_before and is_user_registered_successfully


# ...

def read_app_settings():
    #  بارگذاری تمام تنظیمات
    settings = DB.settings.get_all_settings()
    if settings is None:
        print("read_app_settings() -> settings is None")
        return None

    app_settings.run_at_windows_startup = (
        settings.get(settings_keys.run_app_at_windows_startup, False))
    app_settings.show_on_top = settings.get(settings_keys.show_on_top, False)
    app_settings.show_on_tray_on_exit = (
        settings.get(settings_keys.show_on_system_tray_on_exit, False))

    # self.appSettings["ColorRectFaceDetection"] = QColor(settings.get("ColorRectFaceDetection", "#FFFF0000"))
    # self.appSettings["ColorTextWatermark"] = QColor(settings.get("ColorTextWatermark", "#FF000000"))

    # TODO:
    # desktop_path = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
    app_settings.save_path = settings.get(settings_keys.save_path, ".").strip()
    if app_settings.save_path in ("", "-", "Desktop"):
        pass
        # self.appSettings["SavePath"] = desktop_path # TODO:

    app_settings.db_data_path = (
        settings.get(settings_keys.db_data_path, app_settings.db_data_path))
    DB.database.Connections["CONN_DATA"]["PATH"] = app_settings.db_data_path

    app_settings.num_of_app_exec = int(settings.get(settings_keys.num_of_app_exec, 0))
    if app_settings.num_of_app_exec <= 0:
        app_settings.num_of_app_exec = 1
    else:
        app_settings.num_of_app_exec += 1

    DB.settings.update_setting(settings_keys.num_of_app_exec, app_settings.num_of_app_exec)

    # ...

    print(f"app_settings.run_at_windows_startup = {app_settings.run_at_windows_startup}")
    # print(f"type(app_settings.run_at_windows_startup)= {type(app_settings.run_at_windows_startup)}")  #  <class 'str'>
    print(f"app_settings.show_on_top = {app_settings.show_on_top}")
    print(f"app_settings.show_on_tray_on_exit = {app_settings.show_on_tray_on_exit}")
    print(f"app_settings.save_path = {app_settings.save_path}")
    print(f"app_settings.db_data_path = {app_settings.db_data_path}")
    print(f"app_settings.num_of_app_exec = {app_settings.num_of_app_exec}")

    # ...

    return True


def write_app_settings():
    new_settings = {
        # "RunAppAtWindowsStartup": app_settings.run_at_startup,
        # "ShowOnTop": app_settings.show_on_top,
        # "ShowOnSystemTrayOnExit": app_settings.show_on_tray_on_exit,
        # # "ColorRectFaceDetection": self.appSettings["ColorRectFaceDetection"].name(QColor.HexArgb),
        # # "ColorTextWatermark": self.appSettings["ColorTextWatermark"].name(QColor.HexArgb),
        # "SavePath": app_settings.save_path,
        # "DbDataPath": app_settings.db_data_path,

        settings_keys.run_app_at_windows_startup: app_settings.run_at_windows_startup,
        settings_keys.show_on_top: app_settings.show_on_top,
        settings_keys.show_on_system_tray_on_exit: app_settings.show_on_tray_on_exit,
        # "ColorRectFaceDetection": self.appSettings["ColorRectFaceDetection"].name(QColor.HexArgb),
        # "ColorTextWatermark": self.appSettings["ColorTextWatermark"].name(QColor.HexArgb),
        settings_keys.save_path: app_settings.save_path,
        settings_keys.db_data_path: app_settings.db_data_path,

        #  نیازی به این نیست. در تابع
        #  read_app_settings()
        #  مقدار آن یکی افزایش پیدا کرده و سپس در دیتا بیس نوشته شده است
        # "NumOfAppExec": app_settings.num_of_app_exec,

        }
    print("--------------------------------------------------------------")
    # TODO: بعد از اطمینان از عملکرد صحیح، این دستورات حذف و یا بهینه شوند
    print("new_settings: \n", new_settings)
    if not DB.settings.update_settings(new_settings):
        print("Failed to update settings(write_app_settings())")
    else:
        print("write_app_settings() is Done")
    print("--------------------------------------------------------------")


# ...

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setLayoutDirection(Qt.RightToLeft)
    app.setOrganizationName(company_info.organization_name)
    app.setOrganizationDomain(company_info.organization_domain)

    # چون تنظیماتی که در رجیستری ثبت میشود از نام زیر استفاده میکند، از نام انگلیسی برنامه استفاده کردم
    app.setApplicationName(app_info.application_name_en)

    # --------------------------------------------------------------------------------------

    # با توجه به اهمیت فایل config چنانچه فایل یافت نشد
    # برنامه باید با نمایش یک پیام بسته شود
    status, message = DB.database.connect_to_db_config()
    if not status:
        QMessageBox.critical(None, "خطا", message)
        app.quit()
        exit(-1)

    """
    # تا اینجا موفق به بازکردن دیتابیس config شدیم. مسیر این فایل همیشه ثابت و در
    # کنار فایل اجرایی برنامه هست. کاربر نمیتواند(و نباید) آن را تغییر دهد
    """

    # --------------------------------------------------------------------------------------

    read_app_settings()
    # print("app_settings.db_data_path ===> ", app_settings.db_data_path)   # OK

    is_connected_successfully = DB.database.try_connect_to_db_data(app_settings.db_data_path)
    if not is_connected_successfully:  # خطاها و پیامها در تابع بالا هندل میشوند
        app.quit()
        exit(-1)

    # ...

    is_registered_user = has_login_form_shown_before_and_registered()
    dialog_login = DialogLogin(show_login_page=is_registered_user)

    if dialog_login.exec() != DialogLogin.Accepted:
        # DB.database.close_db_connection()
        # DB.database.close_db_connection("CONN_CONFIG", "CONN_DATA")
        DB.database.close_all_db_connections()

        app.quit()
        exit(-1)

    # ...

    from mainwindow import MainWindow

    splash = QSplashScreen(QPixmap(":/splash.jpg"), Qt.WindowStaysOnTopHint)
    splash.setWindowFlag(Qt.FramelessWindowHint)
    splash.show()

    app.processEvents()  # اجازه میدیم کمی سیستم پردازش کنه

    # ...
    time.sleep(1)  # TODO:
    # ...

    window = MainWindow()
    window.show()

    # ...
    splash.finish(window)
    # ...

    sys.exit(app.exec())
