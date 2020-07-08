import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="ducdb")

mycursor = mydb.cursor()

mycursor.execute("Select * from gamerscredentials")

myresult = mycursor.fetchall()
# myresult = mycursor.getchone() - will return next row of a query result set
for row in myresult:
    print(row)