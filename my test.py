
import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

root = Tk()
root.geometry('500x200')
root.title("Covid Cases")
root.configure(bg = '#49A')

bgImage = PhotoImage(file = r'C:\Users\ajay.kumar\PycharmProjects\untitled\branches-2740419_1920.png')
Label(root, image = bgImage).place(relwidth=1, relheight = 1)

Label(root,text = "Search availibility slot for vaccine",underline=1, font = 'Helvetica 12 underline bold ',padx = 20,pady=5,relief  =FLAT,bg ="light grey",bd=4,anchor='nw').grid(row=0,column=1,padx=10,pady=1)


Label(root,text = "STATE",font ='Cambria',padx = 32,bg = 'LightPink1',fg = 'black',bd = 5,relief = SUNKEN).grid(row = 3,column = 0)
Label(root,text = "DISTRICT",font ='Cambria',padx = 20,bg = 'LightPink1',fg = 'black',bd = 5,relief = SUNKEN).grid(row = 4,column = 0)
state_api = "https://cdn-api.co-vin.in/api/v2/admin/location/states"


state_value = StringVar()
stateentry = Entry(root, textvariable = state_value, bd = 5).grid(row =3, column=1, pady = 5)
print(state_value.get())
dist_value = StringVar()
distentry = Entry(root, textvariable = dist_value, bd = 5).grid(row = 4, column = 1, pady = 5)
print(dist_value.get())

state_ids = requests.get(state_api,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}).json()

def order():

        global lst
        lst = []
        root1 = tk.Tk()
        root1.title("Vaccine Availibility Slot")
        root1.geometry("750x600")
        tree = ttk.Treeview(root1)

        tree['show'] = 'headings'
        s = ttk.Style(root1)

        s.theme_use("clam")
        s.configure(".", font=('Helvetica', 11))
        s.configure("Treeview.Heading", foreground='red', font=('Helvetica', 11, "bold"))

        tree["columns"] = ("CENTER NAME", "AVAILABLE CAPACITY", "DATE","VACCINE", "AGE")

        tree = ttk.Treeview(root1, columns=("CENTER NAME", "AVAILABLE CAPACITY", "DATE", "VACCINE","AGE"), show='headings', height=30)
        tree.pack(side=LEFT)

        tree.column("CENTER NAME", width=220, minwidth=50, anchor=tk.CENTER)
        tree.column("AVAILABLE CAPACITY", width=150, minwidth=50, anchor=tk.CENTER)
        tree.column("DATE", width=150, minwidth=50, anchor=tk.CENTER)
        tree.column("VACCINE", width=150, minwidth=50, anchor=tk.CENTER)
        tree.column("AGE", width=50, minwidth=50, anchor=tk.CENTER)

        tree.heading("CENTER NAME", text="CENTER NAME", anchor=tk.CENTER)
        tree.heading("AVAILABLE CAPACITY", text="AVAILABLE CAPACITY", anchor=tk.CENTER)
        tree.heading("DATE", text="DATE", anchor=tk.CENTER)
        tree.heading("VACCINE", text="VACCINE", anchor=tk.CENTER)
        tree.heading("AGE", text="AGE", anchor=tk.CENTER)

        state = state_value.get().title()
        dist = dist_value.get().title()

        for i in state_ids['states']:

            if (state == i['state_name']):
                Final_state_id = i['state_id']
                print(Final_state_id)



        dist_id = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(Final_state_id)
        dist_id_res = requests.get(dist_id, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}).json()


        for i in dist_id_res['districts']:

            if (dist == i['district_name']):
                Final_district_id = i['district_id']
                print(Final_district_id)

        result_dist = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(
            Final_district_id, datetime.today().strftime('%d-%m-%Y'))
        result_dist_res = requests.get(result_dist, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}).json()



        for i in range(len(result_dist_res['centers'])):
            for j in range(len(result_dist_res['centers'][i]['sessions'])):

                if result_dist_res['centers'][i]['sessions'][j]['available_capacity'] > 0:

                    #print("in loop   : ",result_dist_res['centers'][i]['name'],result_dist_res['centers'][i]['sessions'][j]['available_capacity'])
                    l1 = []
                    l2 = ()
                    l1.append(result_dist_res['centers'][i]['name'])
                    l1.append(result_dist_res['centers'][i]['sessions'][j]['available_capacity'])
                    l1.append(result_dist_res['centers'][i]['sessions'][j]['date'])
                    l1.append(result_dist_res['centers'][i]['sessions'][j]['vaccine'])
                    l1.append(result_dist_res['centers'][i]['sessions'][j]['min_age_limit'])
                    l2 = tuple(l1)
                    #print("tuple",l2)
                    lst.append(l2)

        #print("list",lst)

        for i in range(len(lst)):

            tree.insert(parent='', index=i, iid=i, text='', values=lst[i])



        tree.pack()

        if len(lst)==0:
            messagebox.showinfo("Sorry", "There is no slot available for this location !!")




Label(root,text='Dev : Ajay ',font ='comicsans 6 bold',bd=4).grid(row = 9,column =2)

Button(root,text = "SEARCH",fg = "black",bg="grey",font = 'bold',relief=RAISED,borderwidth=2,command = order).grid(row =6 ,column=1)

root.mainloop()