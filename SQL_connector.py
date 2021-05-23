

import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user  = "root",passwd = "Aj@y56765",database = "Record")


mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE Record")
#
# mycursor.execute("SHOW DATABASES")
#
# for db in mycursor:
#      print(db)
# mycursor.execute("CREATE TABLE Employees (Dob DATE)")
mycursor.execute("CREATE TABLE employees(id VARCHAR(255),empname VARCHAR(255),phone INTEGER(12),salary INTEGER(20))")
#mycursor.execute('SHOW TABLES')
# for table in mycursor:
#     print(table)
#
# mycursor.execute("SELECT * FROM users")
# for i in mycursor:
#     print(i)

#sqlstuff = "INSERT INTO employees(name, email,age) VALUES(%s, %s, %s)"
# record1 = ("Ajay", "ajay.23432@gmail.com", 29)
#
# mycursor.execute(sqlstuff,record1)
#
# mydb.commit()
#
# sqlstuff = "INSERT INTO employees(Emp_Id, email,age) VALUES(%s, %s, %s)"
# records = [
#     ("Abhi","abhi.com",27),
#     ("nisha","nisha.com",23),
#     ("Puja","puja.com",29),
#     ("Mom","mom.com",45),
# ]
#
# mycursor.executemany(sqlstuff,records)
# mydb.commit()

# mycursor.execute('SELECT * FROM users')
# result = mycursor.fetchall()
#
# for res in result:
#     print(res[0]+ "\t" +res[1])

# mycursor.execute("SELECT * FROM users WHERE name '%i%' OR age>5")
# result = mycursor.fetchall()
# for i in result:
#     print(i)

# my_sql = "UPDATE users SET age = 41 WHERE userid = 5"
# mycursor.execute(my_sql)
# mydb.commit()

#
# mycursor.execute("SELECT * FROM users ORDER BY name DESC")
# result = mycursor.fetchall()
# for i in result:
#     print(i)

# remv = "DELETE FROM users WHERE userid=1 "
# mycursor.execute(remv)
#mydb.commit()

