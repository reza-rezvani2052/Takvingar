import DB.database  # حتما باید به اینصورت ایمپورت شوند
# from DB.database import db_config_conn, ConnectionsName

from PySide6.QtSql import QSqlDatabase, QSqlQuery


def get_all_settings():
    settings_map = {}

    query = QSqlQuery(DB.database.Connections["CONN_CONFIG"]["CONN"])
    if not query.exec("SELECT settings_key, value, default_value FROM tbl_settings"):
        print("Error: Could not load settings (get_all_settings())->", query.lastError().text())
        return settings_map

    while query.next():
        settings_key = query.value("settings_key")
        value = query.value("value")
        if value is None or value == "":
            value = query.value("default_value")
        settings_map[settings_key] = value

    return settings_map


def get_setting_by_key(settings_key, default_value=None):
    query = QSqlQuery(DB.database.Connections["CONN_CONFIG"]["CONN"])

    query.prepare("SELECT value, default_value FROM tbl_settings WHERE settings_key = :settings_key")
    query.bindValue(":settings_key", settings_key)

    if not query.exec():
        print("Error: Failed to execute query(get_setting_by_key()) ->", query.lastError().text())
        return default_value

    if query.next():
        value = query.value("value")
        if value is None or value == "":
            value = query.value("default_value")
        return value
    else:
        print(f"settings_key not found: {settings_key}. Returning default value.")
        return default_value


def get_settings_by_keys(keys):
    settings_map = {}

    if not keys:
        return settings_map

    # db = QSqlDatabase.database()
    # if not db.isOpen():
    #     print("Error: Database is not open.")
    #     return settings_map

    placeholders = ', '.join(['?'] * len(keys))
    query_string = f"SELECT settings_key, value, default_value FROM tbl_settings WHERE settings_key IN ({placeholders})"

    query = QSqlQuery(DB.database.Connections["CONN_CONFIG"]["CONN"])
    query.prepare(query_string)
    for key in keys:
        query.addBindValue(key)

    if not query.exec():
        print("Error: Failed to execute query(get_settings_by_keys()) ->", query.lastError().text())
        return settings_map

    while query.next():
        key = query.value("settings_key")
        value = query.value("value")
        if value is None or value == "":
            value = query.value("default_value")
        settings_map[key] = value

    return settings_map


def update_setting(settings_key, value):
    query = QSqlQuery(DB.database.Connections["CONN_CONFIG"]["CONN"])

    query.prepare("UPDATE tbl_settings SET value = :value WHERE settings_key = :settings_key")
    query.bindValue(":value", value)
    query.bindValue(":settings_key", settings_key)

    if not query.exec():
        print("Error: Could not update setting(update_setting()) ->", query.lastError().text())
        return False

    return True


def update_settings(settings_dict):
    db = QSqlDatabase.database(DB.database.Connections["CONN_CONFIG"]["NAME"])
    if not db.isValid() or not db.isOpen():
        print("Error: Database connection is not valid or open(update_settings())")
        return False

    if not db.transaction():
        print("Error: Could not start transaction(update_settings() ->", db.lastError().text())
        return False

    query = QSqlQuery(db)

    for settings_key, value in settings_dict.items():
        query.prepare("UPDATE tbl_settings SET value = :value WHERE settings_key = :settings_key")
        query.bindValue(":value", value)
        query.bindValue(":settings_key", settings_key)

        if not query.exec():
            print("Error: Could not update setting(update_settings()) ->", query.lastError().text())
            db.rollback()
            return False

    if not db.commit():
        print("Error: Could not commit transaction(update_settings()) ->", db.lastError().text())
        db.rollback()
        return False

    return True
