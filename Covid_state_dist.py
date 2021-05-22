

from tkinter import *
from tkinter import messagebox
import requests


root = Tk()
root.geometry('1020x980')
root.title("Covid Cases")
root.configure(bg = '#49A')

bgImage = PhotoImage(file = r'C:\Users\ajay.kumar\PycharmProjects\untitled\corrrrona.png')
Label(root, image = bgImage).place(relwidth=1, relheight = 1)
api_address = "https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true"
api_address_dist = "https://api.covid19india.org/state_district_wise.json"

covid = requests.get(api_address).json()
covid_dist = requests.get(api_address_dist).json()


Label(root,text = "COVID-19 CASES INDIA",underline=0, font = 'mv 10 bold ',padx = 20,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4,anchor='nw').grid(row=0,column=0,padx=10,pady=1)
Label(root,text = "STATE",font ='Cambria',padx = 20,bg = 'LightPink1',fg = 'black',bd = 5,relief = SUNKEN).grid(row = 1,column = 2)
Label(root,text = "CITY",font ='Cambria',padx = 20,bg = 'LightPink1',fg = 'black',bd = 5,relief = SUNKEN).grid(row = 2,column = 2)

#Labels India details
Label(root,text = "Total ACTIVE CASES ",font = 'mv 10 bold ',padx = 15,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4).grid(row=4, column=0)
Label(root,text = "RECOVERED",font = 'mv 10 bold ',padx = 15,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4).grid(row=4, column=1)
Label(root,text = "DEATHS",font = 'mv 10 bold ',padx = 15,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4).grid(row=4, column=2)
Label(root,text = "TOTAL CASES",font = 'mv 10 bold ',padx = 15,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4).grid(row=4, column=3)

#details for for the state
Label(root,text = covid['activeCases'],padx = 12,font = 'Malgun 10 bold',bg = "Aqua",fg = "black",relief=SUNKEN,bd=4).grid(row=5, column=0,pady=10)
Label(root,text = covid['recovered'],padx = 12,font = 'Malgun 10 bold',bg = "Aqua",fg = "black",relief=SUNKEN,bd=4).grid(row=5, column=1)
Label(root,text = covid['deaths'],padx = 12,font = 'Malgun 10 bold',bg = "Aqua",fg = "black",relief=SUNKEN,bd=4).grid(row=5, column=2)
Label(root,text = covid['totalCases'],padx = 12,font = 'Malgun 10 bold',bg = "Aqua",fg = "black",relief=SUNKEN,bd=4).grid(row=5, column=3)

# Labels Details for state

Label(root,text = "REGION",font = 'mv 10 bold ',padx = 45,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4).grid(row=7, column=0,pady=10)
Label(root,text = "TOTAL INFECTED",font = 'mv 10 bold ',padx = 15,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4).grid(row=8, column=0,pady=10)
Label(root,text = "NEW CASES",font = 'mv 10 bold ',padx = 35,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4).grid(row=9, column=0,pady=10)
Label(root,text = "RECOVERED",font = 'mv 10 bold ',padx = 35,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4).grid(row=10, column=0,pady=10)
Label(root,text = "DEATH",font = 'mv 10 bold ',padx = 55,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4).grid(row=11, column=0,pady=10)
Label(root,text = "RECENT DEATH",font = 'mv 10 bold ',padx = 25,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4).grid(row=12, column=0,pady=10)


#Lables details for dist
#Label(root,text = "district Data",font = 'Italic ',padx = 45,pady=5,bd=4).grid(row=6, column=3,pady=10)
Label(root,text = "ACTIVE CASES",font = 'mv 10 bold ',padx = 25,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4).grid(row=7, column=3,pady=10)
Label(root,text = "CONFIRMED CASES",font = 'mv 10 bold ',padx = 10,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4).grid(row=8, column=3,pady=10)
Label(root,text = "DEATH",font = 'mv 10 bold ',padx = 55,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4).grid(row=9, column=3,pady=10)
Label(root,text = "RECOVERED",font = 'mv 10 bold ',padx = 35,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4).grid(row=10, column=3,pady=10)
Label(root,text = "RECENT CASES",font = 'mv 10 bold ',padx = 30,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4).grid(row=11, column=3,pady=10)
Label(root,text = "RECENT DEATH",font = 'mv 10 bold ',padx = 30,pady=5,relief  =SUNKEN,bg ="LightPink1",bd=4).grid(row=12, column=3,pady=10)


state_value = StringVar()
stateentry = Entry(root, textvariable = state_value, bd = 5).grid(row =1, column=3, pady = 10)

city_value = StringVar()
cityentry = Entry(root, textvariable = city_value, bd = 5).grid(row = 2, column = 3, pady = 10)



def order1():

    global state_val

    state_val = state_value.get().title()



    Label(root, text="COVID cases in {}".format(state_val), font=("Comic Sans MS", 10, "italic")).grid(row=6,
                                                                                                             column=0,
                                                                                                             pady=10)
    for i in range(len(covid['regionData'])):

        if covid['regionData'][i]['region'] == state_val:

            Label(root, text= state_val, padx=12, bg="OliveDrab2", fg="black",relief  =SUNKEN,font = 'mv 12 bold').grid(row=7,column=1)
            Label(root, text=covid['regionData'][i]['totalInfected'], padx=12,relief  =SUNKEN,font = 'mv 12 bold ', bg="OliveDrab2", fg="black").grid(row=8, column=1)
            Label(root, text=covid['regionData'][i]['recovered'], padx=14,relief  =SUNKEN,font = 'mv 12 bold ', bg="OliveDrab2",
                  fg="black").grid(row=10, column=1)
            Label(root, text=covid['regionData'][i]['deceased'], padx=20,relief  =SUNKEN,font = 'mv 12 bold ', bg="OliveDrab2",
                  fg="black").grid(row=11, column=1)
            Label(root, text=covid['regionData'][i]['newInfected'], padx=20, relief=SUNKEN, font='mv 12 bold ',
                  bg="OliveDrab2",
                  fg="black").grid(row=9, column=1)
            Label(root, text=covid['regionData'][i]['newDeceased'], padx=20, relief=SUNKEN, font='mv 12 bold ',
                  bg="OliveDrab2",
                  fg="black").grid(row=12, column=1)


def order():

    new_city = city_value.get().title()

    Label(root,text ="COVID cases in {}".format(city_value.get()),font = ("Comic Sans MS", 10, "italic"),padx = 45,pady=5,bd=4).grid(row=6, column=3,pady=10)

    for i in covid_dist:
        try:

            Label(root, text=covid_dist[state_val]["districtData"][new_city]['active'], padx=12, font='Malgun 10 bold', bg="OliveDrab2", fg="black", relief=SUNKEN,
                      bd=4).grid(row=7, column=4, pady=10)

            Label(root, text=covid_dist[state_val]["districtData"][new_city]['confirmed'], padx=12, font='Malgun 10 bold',
                      bg="OliveDrab2", fg="black", relief=SUNKEN,
                      bd=4).grid(row=8, column=4, pady=10)


            Label(root, text= covid_dist[state_val]["districtData"][new_city]['deceased'], padx=12, font='Malgun 10 bold',
                      bg="OliveDrab2", fg="black", relief=SUNKEN,
                      bd=4).grid(row=9, column=4, pady=10)


            Label(root, text=covid_dist[state_val]["districtData"][new_city]['recovered'], padx=12,
                      font='Malgun 10 bold',
                      bg="OliveDrab2", fg="black", relief=SUNKEN,
                      bd=4).grid(row=10, column=4, pady=10)


            Label(root, text=covid_dist[state_val]["districtData"][new_city]['delta']['confirmed'], padx=12,
                      font='Malgun 10 bold',
                      bg="OliveDrab2", fg="black", relief=SUNKEN,
                      bd=4).grid(row=11, column=4, pady=10)


            Label(root, text=covid_dist[state_val]["districtData"][new_city]['delta']['deceased'], padx=12,
                      font='Malgun 10 bold',
                      bg="OliveDrab2", fg="black", relief=SUNKEN,
                      bd=4).grid(row=12, column=4, pady=10)

        except NameError and KeyError:
            messagebox.showinfo("WARNING","Please select state and click OK")
            break




Button(root,text = "OK",fg = "black",bg="grey",font = 'bold',relief=RAISED,borderwidth=5,command = order1).grid(row = 1,column=4,pady=5)
Button(root,text = "OK",fg = "black",bg="grey",font = 'bold',relief=RAISED,borderwidth=5,command = order).grid(row = 2,column=4,pady=5)

Label(root,text='Developer : Ajay Kumar',font ='comicsans 8 bold',bd=4).grid(row = 16,column =4)

Button(root, text="QUIT",font= 'lucida 10 bold', command=root.destroy,relief = RAISED,bd =4,bg = "grey",padx=15).grid(row = 13,column = 2,padx=30)

root.mainloop()