import sqlite3 as sq

with sq.connect(str(input())) as con:
    cur = con.cursor()

    res = cur.execute(f"""SELECT name, cheef FROM danger 
    WHERE workload >= 41 {str(input())} {str(input())} ORDER BY loyalty""").fetchall()

    for i in res:
        print(f'{i[0]} ({i[1]})')
