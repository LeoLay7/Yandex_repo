import sqlite3 as sq

with sq.connect('lms.db') as con:
    cur = con.cursor()

    condition = str(input())
    request = f"SELECT middle_name, first_name, last_name, phone, email FROM user WHERE {condition}"

    res = cur.execute(request).fetchall()
    for i in res:
        print(i)