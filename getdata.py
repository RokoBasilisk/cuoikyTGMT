import mysql.connector as mc
import os

def write_image(data, imagename,idd):
    path = "images/{0}/{1}.png".format(idd,str(imagename))
    with open(path, 'wb') as File:
        File.write(data)
        File.close()


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

for x in result:
    row = dict(zip(connector.column_names,x))
    idlist = os.listdir('images')
    ID = str(row['ID'])
    NAME = str(row['UserName'])
    IMAGE = row['Image']
    if ID not in idlist:
        parent_dir = "D:/SOUCE_CODE/Python/thi/images"
        path = os.path.join(parent_dir,ID)
        os.mkdir(path)
        write_image(IMAGE,NAME,ID)
        print("Đã Thêm vào {0}".format(path))
    else:
        print("Đã có")

