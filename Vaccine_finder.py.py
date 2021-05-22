import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import webbrowser

root = Tk()
root.geometry('500x200')
root.title("SEARCH AVAILABLE SLOT")
root.iconbitmap(r'C:\Users\ajay.kumar\PycharmProjects\untitled\vaccine.ico')

root.configure(bg='grey')

bgImage = PhotoImage(file=r'C:\Users\ajay.kumar\PycharmProjects\untitled\branches-2740419_1920.png')
Label(root, image=bgImage).place(relwidth=1, relheight=1)

Label(root, text="Search availibility slot for vaccine", fg='red', font='Helvetica 12 italic bold ',
      padx=20, pady=5, relief=FLAT, bg="light grey", bd=4, anchor='nw').grid(row=0, column=1, padx=10, pady=1)

Label(root, text="STATE", font='Cambria', padx=32, bg='LightPink1', fg='black', bd=5, relief=GROOVE).grid(row=3,
                                                                                                          column=0)
Label(root, text="DISTRICT", font='Cambria', padx=20, bg='LightPink1', fg='black', bd=5, relief=GROOVE).grid(row=4,column=0)
state_api = "https://cdn-api.co-vin.in/api/v2/admin/location/states"




state_value = StringVar()
dist_value = StringVar()
# stateentry = Entry(root, textvariable=state_value, bd=5).grid(row=3, column=1, pady=5)

state_ids = requests.get(state_api, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}).json()

st_name = []
dist_name = []
Final_state_id = 0
def comboclick(event):
    #print(state_value.get())
    global Final_state_id
    global dist_name
    for i in state_ids['states']:

        if (state_value.get() == i['state_name']):
            Final_state_id = i['state_id']
            #print("final state id {} for {}".format(Final_state_id, i['state_name']))

    dist_id = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(Final_state_id)
    dist_id_res = requests.get(dist_id, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}).json()

    #print("response dist", dist_id_res)

    dist_name = []
    for i in dist_id_res['districts']:

        dist_name.append(i['district_name'])
    #print("diist",dist_name)

    myCombo_dis = ttk.Combobox(root, value=dist_name, textvariable=dist_value)
    myCombo_dis.bind("<<ComboboxSelected>>", comboclickdis)
    myCombo_dis.grid(row=4, column=1)



for i in state_ids['states']:
    st_name.append( i['state_name'])


myCombo = ttk.Combobox(root,value = st_name,textvariable = state_value)
myCombo.bind("<<ComboboxSelected>>",comboclick)
myCombo.grid(row=3,column = 1)

def comboclickdis(event):
    print(dist_value.get())


myCombo_dis = ttk.Combobox(root, value=dist_name, textvariable=dist_value)
myCombo_dis.bind("<<ComboboxSelected>>", comboclickdis)
myCombo_dis.grid(row=4, column=1)


def order():
    global lst
    lst = []

    def func():
        state = state_value.get().title()
        dist = dist_value.get().title()

        flag_st = 0
        st_name = []
        for i in state_ids['states']:

            if (state == i['state_name']):
                Final_state_id = i['state_id']
               # print(Final_state_id)
                dist_id = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(Final_state_id)
                dist_id_res = requests.get(dist_id, headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}).json()

                flag_st = 1

        if flag_st == 0:
            messagebox.showinfo("Sorry", "Please enter a correct state name")

        # print(state_ids['states'])
        #
        # print("state names", st_name)

        flag_dist = 0
        for i in dist_id_res['districts']:

            if (dist == i['district_name']):
                Final_district_id = i['district_id']
                #print(Final_district_id)
                result_dist = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(
                    Final_district_id, datetime.today().strftime('%d-%m-%Y'))
                result_dist_res = requests.get(result_dist, headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}).json()

                flag_dist = 1

        if flag_dist == 0:
            messagebox.showinfo("District not found", "May be district not present or there is a mismatch in spelling")

        for i in range(len(result_dist_res['centers'])):
            for j in range(len(result_dist_res['centers'][i]['sessions'])):

                if result_dist_res['centers'][i]['sessions'][j]['available_capacity'] > 0:
                    # print("in loop   : ",result_dist_res['centers'][i]['name'],result_dist_res['centers'][i]['sessions'][j]['available_capacity'])
                    l1 = []
                    l2 = ()
                    l1.append(result_dist_res['centers'][i]['name'])
                    l1.append(result_dist_res['centers'][i]['address'])
                    l1.append(result_dist_res['centers'][i]['sessions'][j]['available_capacity'])
                    l1.append(result_dist_res['centers'][i]['sessions'][j]['available_capacity_dose1'])
                    l1.append(result_dist_res['centers'][i]['sessions'][j]['available_capacity_dose2'])
                    l1.append(result_dist_res['centers'][i]['sessions'][j]['date'])
                    l1.append(result_dist_res['centers'][i]['sessions'][j]['vaccine'])
                    l1.append(result_dist_res['centers'][i]['sessions'][j]['min_age_limit'])
                    l2 = tuple(l1)

                    lst.append(l2)

        # print("list",lst)


        return lst

    def func_2(lst):
        if len(lst)>0:

            root1 = tk.Tk()
            root1.title("Vaccine Availibility Slot")
            root1.geometry("1320x600")
            root1.iconbitmap(r'C:\Users\ajay.kumar\PycharmProjects\untitled\vaccine.ico')
            tree = ttk.Treeview(root1)

            def callback(url):
                webbrowser.open_new(url)

            link1 = Label(root1, text="Register here for Vaccination", font=('Helvetica 15 underline italic'), fg="blue",
                          cursor="hand2")
            link1.pack(side = TOP)
            link1.bind("<Button-1>", lambda e: callback("https://selfregistration.cowin.gov.in/"))

            tree['show'] = 'headings'
            s = ttk.Style(root1)

            s.theme_use("clam")
            s.configure(".", font=('Helvetica', 11))
            s.configure("Treeview.Heading", foreground='red', font=('Helvetica', 11, "bold"))

            tree["columns"] = ("CENTER NAME", "AVAILABLE CAPACITY", "DATE", "VACCINE", "AGE")

            tree = ttk.Treeview(root1, columns=("CENTER NAME","ADDRESS", "AVAILABLE CAPACITY","DOSE-1 AVAILIBILITY","DOSE-2 AVAILIBILITY","DATE", "VACCINE", "AGE"),
                                show='headings', height=30)
            tree.pack(side=LEFT)

            tree.column("CENTER NAME", width=220, minwidth=50, anchor=tk.CENTER)
            tree.column("ADDRESS", width=220, minwidth=50, anchor=tk.CENTER)
            tree.column("AVAILABLE CAPACITY", width=180, minwidth=50, anchor=tk.CENTER)
            tree.column("DOSE-1 AVAILIBILITY", width=180, minwidth=50, anchor=tk.CENTER)
            tree.column("DOSE-2 AVAILIBILITY", width=180, minwidth=50, anchor=tk.CENTER)

            tree.column("DATE", width=150, minwidth=50, anchor=tk.CENTER)
            tree.column("VACCINE", width=130, minwidth=50, anchor=tk.CENTER)
            tree.column("AGE", width=40, minwidth=50, anchor=tk.CENTER)

            tree.heading("CENTER NAME", text="CENTER NAME", anchor=tk.CENTER)
            tree.heading("ADDRESS", text="ADDRESS", anchor=tk.CENTER)
            tree.heading("AVAILABLE CAPACITY", text="AVAILABLE CAPACITY", anchor=tk.CENTER)
            tree.heading("DOSE-1 AVAILIBILITY", text="DOSE-1 AVAILIBILITY", anchor=tk.CENTER)
            tree.heading("DOSE-2 AVAILIBILITY", text="DOSE-2 AVAILIBILITY", anchor=tk.CENTER)
            tree.heading("DATE", text="DATE", anchor=tk.CENTER)
            tree.heading("VACCINE", text="VACCINE", anchor=tk.CENTER)
            tree.heading("AGE", text="AGE", anchor=tk.CENTER)

            for i in range(len(lst)):

                tree.insert(parent='', index=i, iid=i, text='', values=lst[i])

            scrollbar = ttk.Scrollbar(root1, orient=tk.VERTICAL, command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            #scrollbar.grid(row=0, column=1, sticky='ns')
            scrollbar.pack(side = RIGHT,fill = BOTH)
            tree.pack()
        else:
            messagebox.showinfo("Sorry", "There is no slot available for this location !!")

    a = func()
    func_2(a)


Label(root, text='Dev : Ajay ', font='comicsans 8 bold', bd=4).grid(row=10, column=2)

Button(root, text="SEARCH", fg="black", bg="grey", font='bold', relief=RAISED, borderwidth=4, command=order).grid(row=6,
                                                                                                                  column=1)

root.mainloop()