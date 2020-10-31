import pymysql

server = pymysql.connect(host="localhost", user="demo",passwd="9ToW1d1ZPGfYBbRg")

cursor = server.cursor()

sql = "CREATE DATABASE IF NOT EXISTS koko;"
cursor.execute(sql)


sql = "USE koko;"
cursor.execute(sql)

sql='''CREATE TABLE IF NOT EXISTS owners(id integer not NULL AUTO_INCREMENT,
                                        name varchar(30) NOT NULL,
                                        gender varchar(7),
                                        phone varchar(12),
                                        PRIMARY KEY (id));'''
cursor.execute(sql)

sql="SHOW tables;"
cursor.execute(sql)
print(cursor.fetchall())