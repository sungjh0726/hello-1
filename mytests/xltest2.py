import openpyxl
from pprint import pprint

file = "./test.xlsx"
book = openpyxl.load_workbook(file)
sheet = book.worksheets[0]

# for i in range(65, 65 + 42):
#     print (i, chr(i) + '3')

print( sheet[ str(chr(0 + 66)) + '3' ].value, len(list(sheet.rows)) )

# for i in range(4):
    