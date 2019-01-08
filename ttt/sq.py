import sqlite3

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

conn = sqlite3.connect("t.db")

with conn:
    cur = conn.cursor()
    sql = "insert into Student(name) values(?)"
    cur.execute(sql, '김일수')

    conn.commit()
