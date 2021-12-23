import mysql.connector as mc
import os

db = mc.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "attendance"
)
connector = db.cursor()

sql = "SELECT * FROM user"

connector.execute(sql)


result = connector.fetchall()
fullname = []

for x in result:
    row = dict(zip(connector.column_names,x))
    idlist = os.listdir('images')
    ID = str(row['ID'])
    NAME = str(row['UserName'])
    FULLNAME = str(row['FullName'])
    IMAGE = row['Image']
    fullname.append(FULLNAME)
    

