import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

con = QSqlDatabase('QSQLITE')
con.setDatabaseName('films_db.sqlite')
if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)
else:
    print("Success!")

query = QSqlQuery()
# print(query.exec('SELECT duration FROM films'))
# print(query.first())
#
# print(query.value(0))

query.prepare('select title, genre, duration from films')
if not query.exec_():
    print('Ошибка запроса')
    print(query.lastError())
else:
    while query.next():
        id = query.value(0)
        name = query.value(1)
        age = query.value(2)
        print(id, name, age)