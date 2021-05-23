
from tkinter import *

import mysql.connector

root = Tk()
root.geometry("1000x644")

Mydb = mysql.connector.connect(host = "localhost", user = "root",passwd = "Aj@y56765")
mycursor = Mydb.cursor()

mycursor.execute("CREATE DATABASE Application_form")

mycursor.execute("CREATE TABLE deatils(Fisrt_name VARCHAR(255),lAST_name VARCHAR(255),mobile_mo VARCHAR(255),userid INTEGER AUTO_INCREMENT PRIMARY KEY)")
Mydb.commit()
Label(root,text = "APPLICATION FORM-2020", font = "comicsansms 10 italic",pady=8,relief = SUNKEN).grid(row = 0,column=3)
ftname = Label(root,text = "FIRST_NAME").grid(row = 3,column=2)
Lastname = Label(root,text = "LAST NAME").grid(row = 4,column=2)
Mobileno = Label(root,text = "MOBILE NUMBER").grid(row = 5,column=2)


ftvalue = StringVar()
ltvalue = StringVar()
Mobileno = StringVar()

ftentry = Entry(root,textvariable = ftvalue).grid(row = 3,column=3)
ltentry = Entry(root,textvariable = ltvalue).grid(row = 4,column=3)
mobileentry = Entry(root,textvariable = Mobileno).grid(row = 5,column=3)
def order():
    sqlstuff = "INSERT INTO deatils(Fisrt_name ,lAST_name,mobile_mo ) VALUES(%s,%s,%s)"
    record = (ftvalue.get(),ltvalue.get(),Mobileno.get())
    mycursor.execute(sqlstuff,record)
    Mydb.commit()

Button(root,text = "SUBMIT",command = order).grid(row = 9,column = 6)


root.mainloop()