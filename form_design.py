
from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox as tmsg
import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user  = "root",passwd = "Aj@y56765",database= "personal_info")
mycursor = mydb.cursor()
# mycursor.execute("ALTER TABLE family_info ADD Address VARCHAR(255) ")
# mydb.commit()
#mycursor.execute("CREATE DATABASE Personal_Info")
#mycursor.execute("CREATE TABLE Family_Info(First_Name VARCHAR(255),LAST_NAME VARCHAR(255),email VARCHAR(255),gender VARCHAR(255),userid INTEGER AUTO_INCREMENT PRIMARY)")
mycursor.execute("#CREATE TABLE Family_Info(name VARCHAR(255),email VARCHAR(255),age INTEGER(10),userid INTEGER AUTO_INCREMENT PRIMARY KEY)")

root = Tk()

def order():
    global s
    s = ""
    if Gendervalue.get() == 1:
        s = "MALE"
    elif Gendervalue.get()==2:
        s = "FEMALE"
    elif Gendervalue.get() == 3:
        s = "OTHER"
    # tmsg.showinfo("your Account", f"We have credied {myslider2.get()} dollars to your account")


    sqlstuff = "INSERT INTO Family_info(name, email,last_name,mobile_no,Gender,loan_amount,Address) VALUES(%s, %s, %s,%s,%s,%s,%s)"
    record = (ft_namevalue.get(),email_idvalue.get(),lt_namevalue.get(),mobile_novalue.get(),s,myslider2.get(),addressvalue.get())

    mycursor.execute(sqlstuff,record)
    mydb.commit()
    tmsg.showinfo("Status","SUBMITTED SUCCESSFULLY !!")

root.geometry('1000x800')
root.wm_iconbitmap("privacy_icon_146112.ico")
#frame = Frame(root,borderwidth = 6,bg = 'grey',relief = SUNKEN)
Label(root,text = "APPLICATION FORM-2020", font = 'comicsansms 10 italic ',pady=10,relief  =SUNKEN,bg ="grey",anchor = 'nw').grid(row=0,column=1,padx=20,pady=10)


ft_name = Label(root,text = "FIRST NAME",pady=15).grid(row=1,column=1)
lt_name = Label(root,text = "LAST NAME",pady=15).grid(row=2,column=1)
Gender = Label(root,text = "GENDER",pady = 15).grid(row=3,column=1)
mobile_no = Label(root,text = "MOBILE NUMBER",pady = 15).grid(row=4,column=1)
email_id = Label(root,text = "EMAIL ID",pady = 15).grid(row=5,column=1)
address  = Label(root,text = "ADDRESS", pady = 15).grid(row = 6,column = 1)

ft_namevalue = StringVar()
lt_namevalue = StringVar()
Gendervalue = IntVar()
mobile_novalue = StringVar()
email_idvalue = StringVar()
addressvalue = StringVar()

ftnameentry = Entry(root, textvariable = ft_namevalue).grid(row =1,column=3)
ltnameentry = Entry(root, textvariable = lt_namevalue).grid(row =2,column=3)
#genderentry = Radiobutton(root,text = "MALE",variable= v,value = 1).grid(row =3,column=3)
radio= Radiobutton(root,text = "MALE",padx = 14,variable = Gendervalue,value=1).grid(row=3,column=3)
radio= Radiobutton(root,text = "FEMALE",padx = 14,variable = Gendervalue,value=2).grid(row=3,column=4)
radio= Radiobutton(root,text = "OTHERS",padx = 14,variable = Gendervalue,value=3).grid(row=3,column=5)

mobilenoentry = Entry(root, textvariable = mobile_novalue).grid(row =4,column=3)
emailentry = Entry(root, textvariable = email_idvalue).grid(row =5,column=3)
addressentry = Entry(root,textvariable = addressvalue).grid(row = 6,column=3)

Button(root,text = "SUBMIT RECORD",fg = "blue",bg="grey",padx = 10,pady = 15,command = order,relief=SUNKEN).grid(row=22,column = 5)

Label(root,text = "How much loan You are Applying for ").grid(row=19,column=5)
myslider2 = Scale(root,from_ = 1000, to =4555,orient = VERTICAL,tickinterval = 1000)
myslider2.set(2000)
myslider2.grid(row=20,column=5)


print("valuename",ft_namevalue.get())
print(addressentry)




root.mainloop()
