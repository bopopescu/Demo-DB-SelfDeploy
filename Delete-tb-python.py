import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="ducdb")

mycursor = mydb.cursor()

sql = "delete from gamerscredentials where username='glock-19'"

mycursor.execute(sql)

mydb.commit()