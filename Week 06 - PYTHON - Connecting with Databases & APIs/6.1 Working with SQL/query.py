import mysql.connector
mydb = mysql.connector.connect( 
    host = 'localhost',
    user='root',
    password='0618' 
)
mycursor = mydb.cursor()
# mycursor.execute("select * from test2.test_table")
mycursor.execute("select c1, c5 from test2.test_table")
for i in mycursor.fetchall():
    print(i)
mydb.close()