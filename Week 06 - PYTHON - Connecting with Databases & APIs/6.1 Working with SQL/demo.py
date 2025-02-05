import mysql.connector
#import mysql.connector 
# #create user 'user'@'%' identified by 'password' 
mydb = mysql.connector.connect( 
    host = 'localhost',
    user='root',
    password='0618' 
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)