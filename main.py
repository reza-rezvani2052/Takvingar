def build_ui_and_convert_qrc_to_py():
    from build_ui import convert_qrc_to_py, convert_all_ui_files

    convert_qrc_to_py()
    convert_all_ui_files()


# TODO: در رلیز نهایی برنامه، بعد از ساخت فایل مربوطه، خط زیر غیر فعال شود
build_ui_and_convert_qrc_to_py()

# ----------------------------------------------------------------------------

import time, sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QSplashScreen)

from dialoglogin import DialogLogin

from definitions import *
from DB.database import (db_conn, db_path, try_connect_to_db,
                         update_setting, update_settings,
                         get_all_settings, get_settings_by_keys)


# ...

def has_login_form_shown_before_and_registered() -> bool:
    options_keys = \
        [
            "HasLoginFormShownBefore",
            "IsUserRegisteredSuccessfully"
            # "NonExistentKey"
        ]

    # واکشی تنظیمات
    settings = get_settings_by_keys(options_keys)

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
    settings = get_all_settings()
    if settings is None:
        print("read_app_settings() -> settings is None")
        return None

    app_settings.run_at_startup = settings.get("RunAppAtWindowsStartup", False)
    app_settings.show_on_top = settings.get("ShowOnTop", False)
    app_settings.show_on_tray_on_exit = settings.get("ShowOnSystemTrayOnExit", False)

    # self.appSettings["ColorRectFaceDetection"] = QColor(settings.get("ColorRectFaceDetection", "#FFFF0000"))
    # self.appSettings["ColorTextWatermark"] = QColor(settings.get("ColorTextWatermark", "#FF000000"))

    # TODO: *
    # desktop_path = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
    app_settings.save_path = settings.get("SavePath", ".").strip()

    if app_settings.save_path in ("", "-", "Desktop"):
        pass
        # self.appSettings["SavePath"] = desktop_path # TODO: *

    app_settings.num_of_app_exec = int(settings.get("NumOfAppExec", 0))
    if app_settings.num_of_app_exec <= 0:
        app_settings.num_of_app_exec = 1
    else:
        app_settings.num_of_app_exec += 1

    update_setting("NumOfAppExec", app_settings.num_of_app_exec)

    print(f"app_settings.run_at_startup = {app_settings.run_at_startup}")
    print(f"type(app_settings.run_at_startup)= {type(app_settings.run_at_startup)}")  # TODO : *  <class 'str'>
    print(f"app_settings.show_on_top = {app_settings.show_on_top}")
    print(f"app_settings.show_on_tray_on_exit = {app_settings.show_on_tray_on_exit}")
    print(f"app_settings.save_path = {app_settings.save_path}")
    print(f"app_settings.num_of_app_exec = {app_settings.num_of_app_exec}")

    # اطلاعات کاربر
    # user_infos = self.get_user_info()
    # self.userInfo["LibName"] = user_infos.get("LibName", "")

    return True


def write_app_settings():
    new_settings = {
        "RunAppAtWindowsStartup": app_settings.run_at_startup,
        "ShowOnTop": app_settings.show_on_top,
        "ShowOnSystemTrayOnExit": app_settings.show_on_tray_on_exit,
        # "ColorRectFaceDetection": self.appSettings["ColorRectFaceDetection"].name(QColor.HexArgb),
        # "ColorTextWatermark": self.appSettings["ColorTextWatermark"].name(QColor.HexArgb),
        "SavePath": app_settings.save_path,

        #  نیازی به این نیست. در تابع
        #  read_app_settings()
        #  مقدار آن یکی افزایش پیدا کرده و سپس در دیتا بیس نوشته شده است
        # "NumOfAppExec": app_settings.num_of_app_exec,

    }

    if not update_settings(new_settings):
        print("Failed to update settings.")
    else:
        print("write_app_settings() is Done")


# ...

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setLayoutDirection(Qt.RightToLeft)
    app.setOrganizationName(company_info.organization_name)
    app.setOrganizationDomain(company_info.organization_domain)

    # چون تنظیماتی که در رجیستری ثبت میشود از نام زیر استفاده میکند، از نام انگلیسی برنامه استفاده کردم
    app.setApplicationName(app_info.application_name_en)

    # ...
    # global db_conn
    db_conn, db_path = try_connect_to_db(db_path)
    if db_conn is None:
        app.quit()
        exit(-1)

    # ...

    is_registered_user = has_login_form_shown_before_and_registered()

    dialog_login = DialogLogin(show_login_page=is_registered_user)
    # dialog_login = DialogLogin(show_login_page=True) #TODO: *** test only

    if dialog_login.exec() != DialogLogin.Accepted:
        if db_conn.isOpen():
            db_conn.close()
        app.quit()
        exit(-1)

    #  تابع زیر حتما باید بعد از فرم لاگین باشد
    read_app_settings()

    # ...

    from mainwindow import MainWindow

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
