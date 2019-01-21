import csv, codecs
import pymysql

sql = '''
    insert into Meltop(rank, title, singer, likecnt) values(%s, %s, %s, %s)
'''
def get_conn(db):
    return pymysql.connect(
        host='localhost',
        user='dooo',
        password='dooo!',
        port=3306,
        db=db,
        charset='utf8')

def save(lst):
    conn = get_conn('dadb')

    with conn:
        cur = conn.cursor()
        cur.executemany(sql, lst)



fp = codecs.open("./csv_melon.csv", "r", "utf-8")
reader = csv.reader(fp, delimiter=',', quotechar='"')
lst = []
for i, cells in enumerate(reader):
    if i != 0 and cells[0] != '계':
        lst.append(cells)
        
    if (i % 15 == 0 or cells[0] == '계') and len(lst) > 0:
        save(lst)
        lst.clear()

# del lst[0]
# del lst[len(lst) - 1]
# print(lst)

# save(lst)
