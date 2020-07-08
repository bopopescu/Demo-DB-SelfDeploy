import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="ducdb")

mycursor = mydb.cursor()

# mycursor.execute("Create table gamersCredentials(userName varchar(200), passwd varchar(200))")
mycursor.execute("Show tables")

for tb in mycursor:
    print(tb)