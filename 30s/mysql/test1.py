import pymysql

db = pymysql.Connect(host='localhost', port=3306, user='root', passwd='azusa520', db='kotori', charset='utf8')

cursor = db.cursor()

sql = "SELECT VERSION()"
cursor.execute(sql)

data = cursor.fetchone()
print(data)
db.close()
