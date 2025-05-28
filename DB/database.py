import os

from PySide6.QtGui import QIcon
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import (QMessageBox, QFileDialog)

import DB.settings
import definitions

# ...


conn_config = None
conn_data = None

# اتصال‌های پایگاه داده
Connections = {
    # شامل تنظیمات کاربر، اطلاعات لاگین و داده‌های حساس
    # مسیر فایل زیر نباید تغییر کند و همیشه در کنار فایل اجرایی برنامه باشد
    "CONN_CONFIG":
        {
            "NAME": "connection_config",
            "PATH": "config._db",
            "CONN": conn_config
            },

    #  شامل اطلاعات حسابداری (فاکتورها، مشتری‌ها، تراکنش‌ها، ...)
    # هنگام بکاپ و بازیابی، فقط فایل زیر تحت تاثیر قرار میگیرد و فایل config را
    # دستکاری نمیکنیم
    "CONN_DATA":
        {
            "NAME": "connection_data",
            "PATH": "data.db",
            "CONN": conn_data
            }
    }


# ...
# کدهای مشترک دو تابع زیر در این تابع نوشته شدند
# connect_to_db_config و connect_to_db_data
# تابع زیر از طریق دو تابع فوق فراخوانی میشود
def connect_to_db(key: str) -> bool:
    global Connections

    if not os.path.exists(Connections[key]["PATH"]):
        return False, f"فایل پایگاه داده پیدا نشد:\n{Connections[key]['PATH']}"
    # ...
    Connections[key]["CONN"] = QSqlDatabase.addDatabase(
            "QSQLITE",
            Connections[key]["NAME"]
            )
    Connections[key]["CONN"].setDatabaseName(Connections[key]["PATH"])  # config._db or data.db
    if not Connections[key]["CONN"].open():
        err_msg = f"اتصال به دیتابیس ناموفق بود:\n{Connections[key]['CONN'].lastError().text()}"
        return False, err_msg

    # ...
    # بررسی اینکه فایل واقعاً دیتابیس معتبر SQLite هست
    status, message = is_valid_sqlite_file(key)
    if not status:
        return False, message
    # ...
    # print("inside connect_to_db() = ", Connections[key]["CONN"])
    return True, f"اتصال به پایگاه داده مورد نظر با موفقیت انجام شد:\n{Connections[key]['PATH']}"


def connect_to_db_config() -> tuple[bool, str]:
    return connect_to_db("CONN_CONFIG")


def connect_to_db_data() -> tuple[bool, str]:
    return connect_to_db("CONN_DATA")


def try_connect_to_db_data(initial_path=Connections["CONN_DATA"]["PATH"]):
    global Connections
    _db_data_path = initial_path

    while True:
        status, message = connect_to_db_data()
        if status:
            Connections["CONN_DATA"]["PATH"] = _db_data_path
            definitions.app_settings.db_data_path = _db_data_path
            DB.settings.update_setting(definitions.settings_keys.db_data_path, _db_data_path)
            return True
        # ...

        msg_box = QMessageBox()
        msg_box.setWindowTitle("خطا")
        msg_box.setText(
                message + "\n\n" +
                "آیا مایل به بازیابی پایگاه داده از طریق انتخاب نسخه پشتیبان هستید؟"
                )
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowIcon(QIcon(":/app-icon.jpg"))

        yes_button = msg_box.addButton("بله", QMessageBox.YesRole)
        no_button = msg_box.addButton("خیر", QMessageBox.NoRole)
        msg_box.setDefaultButton(yes_button)
        msg_box.exec()

        if msg_box.clickedButton() == yes_button:
            _db_data_path = choose_database_file()
            if not _db_data_path:
                break  # کاربر انتخاب نکرد → خروج از حلقه و پایان برنامه

            definitions.app_settings.db_data_path = _db_data_path
            DB.database.Connections["CONN_DATA"]["PATH"] = _db_data_path
        else:
            break

    return False


def choose_database_file():
    file_path, _ = QFileDialog.getOpenFileName(
            None,
            "انتخاب فایل پایگاه داده",
            ".",
            "SQLite Database Files (*.db);;All Files (*)"
            )
    return file_path


def is_valid_sqlite_file(key: str) -> tuple[bool, str]:
    # بررسی وجود کلید
    if key not in Connections:
        return False, f"❌ کلید '{key}' در لیست اتصال‌ها یافت نشد."

    # path = Connections[key]["PATH"]
    path = Connections[key].get("PATH")
    conn = Connections[key].get("CONN")

    # بررسی اندازه فایل
    if not os.path.isfile(path) or os.path.getsize(path) == 0:
        return False, f"فایل انتخاب ‌شده وجود ندارد یا خالی است:\n{path}"

    # بررسی ساختار پایگاه داده
    query = QSqlQuery(conn)
    if not query.exec("SELECT name FROM sqlite_master WHERE type='table'"):
        Connections[key]["CONN"].close()
        QSqlDatabase.removeDatabase(Connections[key]["CONN"].connectionName())
        return False, f"فایل پایگاه داده معتبر نیست:\n{path}"

    # بررسی وجود جدول خاص
    # expected_table = "tbl_settings"  # یا هر جدول دلخواه
    # table_found = False
    # while query.next():
    #     if query.value(0) == expected_table:
    #         table_found = True
    #         break
    # if not table_found:
    #     return False, f"فایل پایگاه داده معتبر است، اما جدول مورد انتظار وجود ندارد:\n{path}"

    # اگر پایگاه داده حداقل یک جدول داره
    if not query.next():
        return False, f"پایگاه داده جدول ندارد:\n{path}"

    return True, "پایگاه داده معتبر است"


def close_all_db_connections():
    for key, conn_info in Connections.items():
        conn = conn_info.get("CONN")
        if conn:
            try:
                conn.close()
                print(f"Connection '{key}' closed.")
            except Exception as e:
                print(f"Error closing '{key}': {e}")
    # Connections.clear()


def close_db_connection(*keys):
    # بستن اتصال‌های مشخص‌شده یا همه‌ی اتصال‌ها در صورت نبود آرگومان

    if not keys:
        close_all_db_connections()
    else:
        for key in keys:
            conn_info = Connections.get(key)
            if conn_info:
                conn = conn_info.get("CONN")
                if conn:
                    try:
                        conn.close()
                        print(f"Connection '{key}' closed.")
                    except Exception as e:
                        print(f"Error closing '{key}': {e}")
                else:
                    print(f"No active connection object in '{key}'.")
                del Connections[key]  # ???
            else:
                print(f"No connection entry for '{key}'.")
