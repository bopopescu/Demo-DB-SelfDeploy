import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="ducdb")

mycursor = mydb.cursor()

def insert_userInfo(userName,country,age):
    sqlfrom =  "insert into userinfo(userName,country,age) values(%s,%s,%s)"

    info = [(userName,country,age)]

    mycursor.executemany(sqlfrom,info)

    mydb.commit()

def insert_gamersCredentials(userName, passwd):
    sqlfrom = "insert into gamerscredentails(userName,passwd) values(%s,%s)"

    credentials = [(userName,passwd)]

    mycursor.executemany(sqlfrom, credentials)

    mydb.commit()

