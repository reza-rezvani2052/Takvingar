import os
from PySide6.QtSql import QSqlDatabase, QSqlQuery


def connect_to_database(db_path):
    if not os.path.exists(db_path):
        # QMessageBox.critical(None, "خطا", f"فایل دیتابیس پیدا نشد:\n{db_path}")
        return None

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(db_path)

    if not db.open():
        # QMessageBox.critical(None, "خطا در اتصال", f"اتصال به دیتابیس ناموفق بود:\n{db.lastError().text()}")
        return None

    # ...

    # بررسی اینکه فایل واقعاً دیتابیس معتبر SQLite هست
    query = QSqlQuery(db)
    if not query.exec("SELECT name FROM sqlite_master WHERE type='table'"):
        db.close()
        QSqlDatabase.removeDatabase(db.connectionName())
        return None

    # ...

    return db


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
