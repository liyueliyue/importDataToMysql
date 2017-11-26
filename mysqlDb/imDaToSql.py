import xlrd,os
from mysqlDb.mysqlClass import DB

baseDir = os.path.dirname(__file__)
baseDir = str(baseDir)
baseDir = baseDir.replace('\\','/')
base = baseDir.split('/mysqlDb')[0]
filePath = base + '/customers.xlsx'
# print(filePath)
wb = xlrd.open_workbook(filePath)
sheet = wb.sheet_by_index(0)
# print(sheet.row(1)[0].value)
# print(sheet.row(1)[1].value)
# print(sheet.row(1)[2].value)
# print(sheet.row(1)[3].value)
# print(sheet.row(1)[4].value)
# print(sheet.row(1)[5].value)
db =DB()
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        name = sheet.row(row)[col].value
        age = sheet.row(row)[col].value
        address = sheet.row(row)[col].value
        date = sheet.row(row)[col].value
        sendGood = sheet.row(row)[col].value
        number = sheet.row(row)[col].value
        # customer = {'name':name,'age':age,'address':address,'date':date,'sendGood':sendGood,'number':number}
        # db.insertData(table_name='customers',test_data=customer)
        print(name,age,address,sendGood,number)
        # print('%7s'%sheet.row(row)[col].value,'\t',end='')