from PySide6.QtSql import QSqlQuery
from datetime import datetime

def log_action(action):
    now = datetime.now().isoformat()
    query = QSqlQuery()
    query.prepare("INSERT INTO history (action, timestamp) VALUES (?, ?)")
    query.addBindValue(action)
    query.addBindValue(now)
    return query.exec()

def get_all_history():
    query = QSqlQuery("SELECT id, action, timestamp FROM history ORDER BY id DESC")
    results = []
    while query.next():
        results.append({
            "id": query.value(0),
            "action": query.value(1),
            "timestamp": query.value(2)
        })
    return results
