from functools import reduce
import sys, os
# sys.path.insert(0, '/Users/jade/workspace/python/hello')
print("------->>", sys.path)
sys.path.insert(0, '../')
print("------->>", sys.path)

print("pppppppp>>", __file__)
print("pppppppp>>", os.path.dirname(__file__))
print("pppppppp>>", os.path.join(os.path.dirname(__file__), '..'))
print("QQQQQQQ:>>", os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("=======>>", os.getcwd(), __file__)
apath = os.path.abspath(__file__)
dirname = os.path.dirname
print("=======>>", apath, dirname(dirname(apath) + "/.."))

print("000000000000>>", os.getcwd())
from Student import Student
# import Student


def printlist(lst):
    for i, l in enumerate(lst):
        print( "{}\t{}".format(i+1, l) )



students = []
with open('/Users/jade/workspace/python/hello/students.csv', 'r') as file:
    for i,f in enumerate(file):
        if i == 0: continue
        # print(i, f)
        students.append( Student(f) )

students.sort(key = lambda stu: stu.score, reverse = True)

m = map(lambda stu: stu.tgrade(), students)
list(m)

total_score = reduce(lambda x, y: (x if type(x) == int else x.score) + y.score, students)
print("tttttttttt>>", total_score, total_score / 10)

print("석차\t이름\t성별\t나이\t학점")
print("----\t------\t----\t----\t----")
printlist(students)

print("\n----------- Top 5 -----------")
for i, s in enumerate(students):
    if i >= 5: break
    print(s.name, s.score)

# print("GGG>>", g_grade)




