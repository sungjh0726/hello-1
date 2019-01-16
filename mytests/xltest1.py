import openpyxl
from pprint import pprint

file = "./test.xlsx"
book = openpyxl.load_workbook(file)
sheet = book.worksheets[0]

data = []
for r in sheet.rows:
    data.append([ r[0].value, r[1].value, r[3].value ])

del data[0]
del data[0]

data = sorted(data, key=lambda x: x[2], reverse=True)
pprint(data)

last = len(data) - 1
print(data[last][2] / 3)