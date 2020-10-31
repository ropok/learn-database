import pymysql

#initialize empty html string
htmlString=""

#create an HTML HEAD
def headhtml (htmlString):
    htmlString+="<!DOCTYPE html>\n<html lang='en'>\n<head>\n<title>Owners of Pets</title>\n</head>\n<body>"
    return(htmlString)

#create an HTML footer
def foothtml(htmlString):
    htmlString+="</body>\n</html>"
    return (htmlString)

#query the database
def ownerquery():
    print("start")
    db = pymysql.connect(host="localhost", user="demo",passwd="9ToW1d1ZPGfYBbRg", db="person")
    cursor = db.cursor()
    sql="SELECT * FROM name;"
    cursor.execute(sql)
    owners = cursor.fetchall()
    sql = "SELECT column_name from information_schema.COLUMNS where TABLE_NAME='name';"
    cursor.execute(sql)
    columns = cursor.fetchall()
    print(columns)
    return(owners, columns)
def ownersTable(owners_list, column_names, html):
    html+="<table border='1'>"
    html+="<tr>"
    i=0
    for name in column_names:
        html+="<th>"+name[0]+"</th>"
        i+=1
    html+="</tr>"
    # for owner in owners_list:
    #     html+="<tr>"
    #     r=0
    #     while r<i:
    #         html+="<td>{0}</td>".format(owner[r])
    #         r+=1
    #     html+="</tr>"
    html+="</table>"
    return(html)

if __name__=="__main__":
    htmlString=headhtml(htmlString)
    (owners, headers)= ownerquery()
    htmlString = ownersTable(owners, headers, htmlString)
    #write to file
    outf = open("rendering.html","w")
    outf.write(htmlString)
    outf.close()