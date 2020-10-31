import pymysql
def load_owners(cursor):
    owners_data=open("name.txt")
    for rowline in owners_data:
        row=rowline.split(",")
        sql="INSERT INTO name(first_name, last_name) VALUES('{}','{}');".format(row[1],row[2])
        cursor.execute(sql)
    cursor.execute("SELECT * from name;")
    print(cursor.fetchall())


if __name__ == "__main__":
    db = pymysql.connect(host="localhost", user="demo",passwd="9ToW1d1ZPGfYBbRg", db="person")
    cursor=db.cursor()
    load_owners(cursor)
    db.commit()
    db.close()