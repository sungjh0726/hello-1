import pymysql
import t_util as tu


def get_conn(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='dooo!',
        port=3306,
        db=db,
        charset='utf8')


conn_dooodb = get_conn('dooodb')
# conn_dadb = get_conn('dadb')
conn_dadb = tu.get_mysql_conn('dadb')

print(tu.get_count(conn_dooodb, 'Subject')[0])

# read from source db
with conn_dooodb:
    cur = conn_dooodb.cursor()
    sql = "select id, name, prof, classroom from Subject"

    cur.execute(sql)
    rows = cur.fetchall()

# write to target db
with conn_dadb:
    cur = conn_dadb.cursor()
    cur.execute('truncate table Subject')

    sql = '''insert into Subject(id, name, prof, classroom)
                          values(%s, %s, %s, %s)'''
    cur.executemany(sql, rows)
    print("AffectedRowCount is", cur.rowcount)
    conn_dadb.commit()
