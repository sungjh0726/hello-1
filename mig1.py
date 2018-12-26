# coding=utf-8
import cx_Oracle

# connection = cx_Oracle.connect("hr/hrpw@localhost:1521/xe")
connection = cx_Oracle.connect("hr", "hrpw", "localhost:1521/xe")

# cursor를 만들어줍니다
cursor = connection.cursor()

query = ''' select * from Departments ''' 

# 실행을 시킵니다.
cursor.execute(query)

# 아래와 같이 차례대로 불러온 컬럼명르 잡아주게 되면 개별 변수에 차례대로 값이 들어가게 됩니다.
for id, name, mgr in cursor:
    print("Values : ", id, name, mgr)
