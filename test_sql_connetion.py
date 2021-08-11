from os import name
import mysql.connector
mydb=mysql.connector.connect(

    host="localhost",
    user="akhil_db",
    password="akhil@123",
    database='mynewdb'
)
mycursor = mydb.cursor()

#mycursor.execute("Create database  mynewdb;")
#mycursor.execute("Show Database")
#mycursor.execute("create table customers (name varchar(50),age int ,id int);")
# for x in mycursor:


#     print(x)

query="insert into "