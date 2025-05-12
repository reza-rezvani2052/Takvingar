import os
import bcrypt

from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import (QMessageBox, QFileDialog)
from PySide6.QtGui import QIcon

# ...


db_conn = None
db_path = "takvingar.db"


# ...


def connect_to_database(db_path):
    global db_conn

    if not os.path.exists(db_path):
        # QMessageBox.critical(None, "خطا", f"فایل دیتابیس پیدا نشد:\n{db_path}")
        return None

    db_conn = QSqlDatabase.addDatabase("QSQLITE")
    db_conn.setDatabaseName(db_path)

    if not db_conn.open():
        # QMessageBox.critical(None, "خطا در اتصال", f"اتصال به دیتابیس ناموفق بود:\n{db.lastError().text()}")
        return None

    # ...

    # بررسی اینکه فایل واقعاً دیتابیس معتبر SQLite هست
    query = QSqlQuery(db_conn)
    if not query.exec("SELECT name FROM sqlite_master WHERE type='table'"):
        db_conn.close()
        QSqlDatabase.removeDatabase(db_conn.connectionName())
        return None

    # ...

    return db_conn


# TODO:?
def create_tables():
    # ایجاد همه جدول‌ها
    QSqlQuery().exec(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
        """
    )
    QSqlQuery().exec(
        """
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT
        )
        """
    )
    QSqlQuery().exec(
        """
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT,
            timestamp TEXT
        )
        """
    )


# --------------------------------------------------------------------------------

def choose_database_file():
    file_path, _ = QFileDialog.getOpenFileName(
        None,
        "انتخاب فایل پایگاه داده",
        ".",
        "SQLite Database Files (*.db);;All Files (*)"
    )
    return file_path


def try_connect_to_db(initial_path):
    global db_path
    global db_conn

    _db_path = initial_path

    while True:
        db_conn = connect_to_database(_db_path)

        if db_conn is not None:
            db_path = _db_path
            return db_conn, _db_path
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

        if msg_box.clickedButton() == yes_button:
            _db_path = choose_database_file()
            if not _db_path:
                break  # کاربر انتخاب نکرد → خروج از حلقه و پایان برنامه
        else:
            break

    return None, None


# --------------------------------------------------------------------------------

def add_user_to_db(username, password, pass_hint, access_level=None) -> tuple[bool, str]:
    # تبدیل هش به رشته (decode)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    query = QSqlQuery()
    query.prepare("""
        INSERT INTO tbl_users (username, password, pass_hint, access_level)
        VALUES (:username, :password, :pass_hint, :access_level)
    """)
    query.bindValue(":username", username)
    query.bindValue(":password", hashed_password)
    query.bindValue(":pass_hint", pass_hint)
    query.bindValue(":access_level", access_level)

    # print("hashed_password = ", hashed_password)

    if not query.exec():
        error = query.lastError().text()
        if "UNIQUE constraint failed" in error:
            return False, "این نام کاربری قبلاً ثبت شده است."
        return False, f"خطا در افزودن کاربر: {error}"

    return True, "کاربر با موفقیت اضافه شد."


def get_all_username():
    list_usernames = []

    query = QSqlQuery("SELECT username FROM tbl_users")
    if not query.exec():
        print("Error: ", query.lastError().text())
        return None

    while query.next():
        list_usernames.append(query.value("username"))

    return list_usernames


def check_password(username: str, password: str) -> bool:
    query = QSqlQuery()
    query.prepare("SELECT password FROM tbl_users WHERE username = :username")
    query.bindValue(":username", username)

    if not query.exec():
        print("خطا در اجرای کوئری:", query.lastError().text())
        return False

    if query.next():
        stored_hashed_password = query.value(0)  # رشته‌ی هش شده
        if isinstance(stored_hashed_password, str):
            stored_hashed_password = stored_hashed_password.encode('utf-8')

        if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
            return True

    return False


def get_pass_hint(username):
    query = QSqlQuery()
    query.prepare("SELECT pass_hint FROM tbl_users WHERE username = :username")
    query.bindValue(":username", username)

    if not query.exec():
        return "Error: " + query.lastError().text()

    if query.next():
        text_pass_hint = query.value(0)
    else:
        text_pass_hint = "موردی یافت نشد"

    return text_pass_hint


# --------------------------------------------------------------------------------

def get_all_settings():
    settings_map = {}

    query = QSqlQuery("SELECT key, value, default_value FROM tbl_settings")
    if not query.exec():
        print("Error: Could not load settings ->", query.lastError().text())
        return settings_map

    while query.next():
        key = query.value("key")
        value = query.value("value")
        if value is None:  # TODO: change by me  ----->  or value.isNull():
            value = query.value("default_value")
        settings_map[key] = value

    return settings_map


def get_setting_by_key(key, default_value=None):
    query = QSqlQuery()
    query.prepare("SELECT value, default_value FROM tbl_settings WHERE key = :key")
    query.bindValue(":key", key)

    if not query.exec():
        print("Error: Failed to execute query ->", query.lastError().text())
        return default_value

    if query.next():
        value = query.value("value")
        if value is None or value.isNull():
            value = query.value("default_value")
        return value
    else:
        print(f"Key not found: {key}. Returning default value.")
        return default_value


def get_settings_by_keys(keys):
    settings_map = {}

    if not keys:
        return settings_map

    db = QSqlDatabase.database()
    if not db.isOpen():
        print("Error: Database is not open.")
        return settings_map

    placeholders = ', '.join(['?'] * len(keys))
    query_string = f"SELECT key, value, default_value FROM tbl_settings WHERE key IN ({placeholders})"

    query = QSqlQuery()
    query.prepare(query_string)
    for key in keys:
        query.addBindValue(key)

    if not query.exec():
        print("Error: Failed to execute query ->", query.lastError().text())
        return settings_map

    while query.next():
        key = query.value("key")
        value = query.value("value")
        if value is None or value == "":  # value.isNull():   TODO: ??? change by me
            value = query.value("default_value")
        settings_map[key] = value

    return settings_map


def update_setting(key, value):
    query = QSqlQuery()
    query.prepare("UPDATE tbl_settings SET value = :value WHERE key = :key")
    query.bindValue(":value", value)
    query.bindValue(":key", key)

    if not query.exec():
        print("Error: Could not update setting ->", query.lastError().text())
        return False

    return True


def update_settings(settings_dict):
    db = QSqlDatabase.database()
    query = QSqlQuery()

    if not db.transaction():
        print("Error: Could not start transaction ->", db.lastError().text())
        return False

    for key, value in settings_dict.items():
        query.prepare("UPDATE tbl_settings SET value = :value WHERE key = :key")
        query.bindValue(":value", value)
        query.bindValue(":key", key)

        if not query.exec():
            print("Error: Could not update setting ->", query.lastError().text())
            db.rollback()
            return False

    if not db.commit():
        print("Error: Could not commit transaction ->", db.lastError().text())
        db.rollback()
        return False

    return True

# --------------------------------------------------------------------------------
