from PySide6.QtSql import QSqlQuery

def set_setting(key, value):
    query = QSqlQuery()
    query.prepare("REPLACE INTO settings (key, value) VALUES (?, ?)")
    query.addBindValue(key)
    query.addBindValue(value)
    return query.exec()

def get_setting(key):
    query = QSqlQuery()
    query.prepare("SELECT value FROM settings WHERE key = ?")
    query.addBindValue(key)
    if query.exec() and query.next():
        return query.value(0)
    return None
