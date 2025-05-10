from PySide6.QtSql import QSqlQuery

def add_user(username, password):
    query = QSqlQuery()
    query.prepare("INSERT INTO users (username, password) VALUES (?, ?)")
    query.addBindValue(username)
    query.addBindValue(password)
    return query.exec()

def get_user(username):
    query = QSqlQuery()
    query.prepare("SELECT id, username, password FROM users WHERE username = ?")
    query.addBindValue(username)
    if query.exec() and query.next():
        return {
            "id": query.value(0),
            "username": query.value(1),
            "password": query.value(2)
        }
    return None
