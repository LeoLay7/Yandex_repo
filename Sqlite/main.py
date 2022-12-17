import sqlite3
import sqlite3 as sq


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


with sq.connect('test.db') as con:
    con.row_factory = sqlite3.Row
    cursor = con.cursor()


    #     cur.execute("DROP TABLE IF EXISTS users")
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    sex INTEGER DEFAULT 1 NOT NULL,
    old INTEGER,
    score INTEGER
    )""")
    #    user_id INTEGER PRIMARY KEY,
    con.commit()

    def lower_string(word: str):
        return word.lower()

    con.create_function('mylower', 1, lower_string)


    print(cursor.execute(f"SELECT Name, sex, old FROM Users WHERE mylower(Name) = mylower('арТеМ')").fetchall())
    print(cursor.description)

    cursor.close()

    # for result in cur:
    #     print(result)
