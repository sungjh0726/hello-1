import pymysql
import random

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")

first_names = list("건성현욱정민현주희진영래주동혜도모영진선재현호시우인성마무병별솔하라")

nums = list("0123456789" * 4)
alphas = list("abcdefghijklmnopqrstuvwxyz" * 4)
years = list(range(80,90))
monthes = list(range(1,13))
days = list(range(1,32))
days30 = list(range(1,31))
days28 = list(range(1,29))

d30m = (4,6,9,11)

def make_birth():
    y = random.choice(years)
    m = random.choice(monthes)
    d = random.choice(days)
    if m == 2 and d > 28:
        d = random.choice(days28)
    elif m in d30m and d > 30:
        d = random.choice(days30)

    return "{}{:02d}{:02d}".format(y, m, d)

def nn(n):
    return "".join(random.sample(nums, n))

def aa(n):
    return "".join(random.sample(alphas, n))

def make_data():
    sung = random.choice(fam_names)
    name = "".join(random.sample(first_names, 2))
    # print(type(sung), type(name))
    tel = "010-{}-{}".format(nn(4), nn(4))
    ri = random.randrange(5, 10)
    email = "{}@gmail.com".format(aa(ri))
    tt = random.choice(monthes)
    return (sung + name, tel, email, make_birth(), tt)


data = []
for i in range(0, 10):
    data.append(make_data())

print(data)

conn = pymysql.connect(host='localhost', port=3306, user='dooo',
                       password='dooo!', db='dooodb', charset='utf8')

with conn:
    cur = conn.cursor()
    sql = "insert into Student(name, tel, email,birth,tt) values(%s,%s,%s,%s,%s)"
    cur.executemany(sql, data)

    print("******", cur.rowcount)
    conn.commit()

# curs = conn.cursor()
# sql = "select * from Student"
# curs.execute(sql)
# rows = curs.fetchall()
# print(rows)  
# conn.close()
