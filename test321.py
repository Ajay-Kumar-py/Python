
from tkinter import *
from tkinter import messagebox
import mysql.connector




def ok():

    id = e1.get()
    empname = e2.get()
    phone = e3.get()
    salary = e4.get()


    mysqldb = mysql.connector.connect(host="localhost", user="root", password="Aj@y56765", database="record")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO employees (id,empname,phone,salary) VALUES (%s, %s, %s, %s)"
        val = (id,empname, phone, salary)
        mycursor.execute(sql, val)
        mysqldb.commit()

        lastid = mycursor.lastrowid
        print("lastid", lastid)
        messagebox.showinfo("information", "Record inserted successfully...")
        #e1.delete(0, END)
        #e1.insert(END, lastid)
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e2.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        messagebox.showinfo("information", e)
        mysqldb.close()

def order():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="Aj@y56765", database="record")
    mycursor = mysqldb.cursor()
    Delete_all_rows = """truncate table employees """
    mycursor.execute(Delete_all_rows)
    mysqldb.commit()
    MsgBox=messagebox.askquestion("information", "Are you sure to delete all records",icon= 'warning')

    if MsgBox == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')



def order1():

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="Aj@y56765", database="record")
    mycursor = mysqldb.cursor()
    temp = str(e5.get())
    print(type(e5.get()))
    mycursor.execute("SELECT id FROM employees ")
    k = mycursor.fetchall()
    print("k",k)
    l = []
    for i in k:
        l = l + list(i)
    print("l",l)

    if temp in l:

        mycursor.execute("SELECT * FROM employees WHERE id = {}".format(temp))

        myresult = mycursor.fetchall()
        print(myresult)
        print(type(myresult))


        t.insert(INSERT,"ID  - {}\n".format(myresult[0][0]))
        t.insert(INSERT, "Name  - {}\n".format(myresult[0][1]))
        t.insert(INSERT, "Phone  - {}\n".format(myresult[0][2]))
        t.insert(INSERT, "Salary  - {}\n".format(myresult[0][3]))

    else:
        messagebox.showinfo('Sorry', 'Employee not present in directory')

root = Tk()
root.title("Employee Registation")
root.geometry("650x550")
global e1
global e2
global e3
global e4
Label(root, text="Employee ID").place(x=10, y=10)
Label(root, text="Employee Name").place(x=10, y=40)
Label(root, text="phone").place(x=10, y=70)
Label(root, text="Salary").place(x=10, y=100)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

Button(root, text="Add", command=ok, height=3, width=13).place(x=10, y=140)

Button(root, text="Delete All Record", command=order, height=3, width=13).place(x=10, y=200)

Label(root, text="Enter ID get the details of employees",relief  =SUNKEN,bg = "blue",font = 'mv 10 bold').place(x=10, y=260)
e5 = Entry(root)
e5.place(x=255, y=260)

Button(root, text="Find", command=order1, height=1, width=3).place(x=380, y=258)

t = Text(root, width=50, height=10, bg="light cyan")
t.place(x=10,y=290)
root.mainloop()