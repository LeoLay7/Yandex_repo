import sqlite3 as sq

with sq.connect('lms.db') as con:
    cur = con.cursor()

    request = f"""SELECT us.first_name, us.birth_date, sol.created_at FROM solution sol JOIN user us ON sol.author_id = us.id 
WHERE sol.status_id = (SELECT id FROM solution_status WHERE status LIKE 'Зачтено') and sol.task_id = '{str(input())}'
AND us.birth_date BETWEEN '1970-01-01' and '2000-01-01'
ORDER BY sol.created_at, us.first_name"""

    res = cur.execute(request).fetchall()

    for i in res:
        print(i)