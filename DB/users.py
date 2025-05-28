import bcrypt

import DB.database
# from DB.database import db_config_path

from PySide6.QtSql import QSqlQuery


def add_user_to_db(username, password, pass_hint, access_level=None) -> tuple[bool, str]:
    # تبدیل هش به رشته (decode)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    query = QSqlQuery(DB.database.Connections["CONN_CONFIG"]["CONN"])
    query.prepare(
        """
        INSERT INTO tbl_users (username, password, pass_hint, access_level)
        VALUES (:username, :password, :pass_hint, :access_level)
        """
        )
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


def check_password(username: str, password: str) -> bool:
    query = QSqlQuery(DB.database.Connections["CONN_CONFIG"]["CONN"])

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
    query = QSqlQuery(DB.database.Connections["CONN_CONFIG"]["CONN"])

    query.prepare("SELECT pass_hint FROM tbl_users WHERE username = :username")
    query.bindValue(":username", username)

    if not query.exec():
        return "Error: " + query.lastError().text()

    if query.next():
        text_pass_hint = query.value(0)
    else:
        text_pass_hint = "موردی یافت نشد"

    return text_pass_hint


def get_all_username():
    list_usernames = []

    query = QSqlQuery(DB.database.Connections["CONN_CONFIG"]["CONN"])
    if not query.exec("SELECT username FROM tbl_users"):
        print("Error(get_all_username()): -> ", query.lastError().text())
        return None

    while query.next():
        list_usernames.append(query.value("username"))

    return list_usernames
