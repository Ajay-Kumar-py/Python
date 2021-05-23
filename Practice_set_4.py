
from tkinter import *


class Table:

    def __init__(self ,root):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):

                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial' ,16 ,'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])





lst = []
for i in range(3):
    l1 = []
    l = ()
    n = int(input("Enter {} no").format(i))
    s = str(input("Enter {} char").format(i))
    s1 = str(input("Enter {} char").format(i))
    l1.append(n)
    l1.append(s)
    l1.append(s1)

    l = tuple(l1)

    lst.append(l)
print(lst)

total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()
t = Table(root)
root.mainloop()

