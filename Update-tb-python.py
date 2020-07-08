import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="ducdb")

mycursor = mydb.cursor()

sql = "Update gamerscredentials set passwd='shootYouDown' where userName='glock-19'"

mycursor.execute(sql)

mydb.commit()