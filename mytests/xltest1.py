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
# print(data)
for i in range(65, 65 + 42):
    print (i, chr(i) + '3')
print( sheet[ str(chr(0 + 66)) + '3' ].value, len(sheet.rows) )

data = sorted(data, key=lambda x: x[2], reverse=True)
# pprint(data)

# for i in range(4):
    