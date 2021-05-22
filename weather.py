
import requests
from tkinter import *
import tkinter.messagebox as tmsg
from datetime import *
from PIL import ImageTk,Image

root = Tk()
root.geometry("625x540")
root.title("Weather Report")

api_address = "https://api.openweathermap.org/data/2.5/weather?q=Bangalore&appid=7a48276f191b32447ccf805e4dab612f"

bgImage = PhotoImage(file = r'C:\Users\ajay.kumar\PycharmProjects\untitled\corrrrona.png')
Label(root, image = bgImage).place(relwidth=1, relheight = 1)

def order():
    city = city_value.get().capitalize()

# city = input("Enter City Name : ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7a48276f191b32447ccf805e4dab612f"
    # print(url)
    json_data = requests.get(url).json()
    print((json_data))
    curr_temp = json_data['main']['temp']
    temp =  curr_temp-273.15
    Label(root,text = round(temp,2),padx = 12,font = 'Malgun 10 bold',bg = "turquoise1",fg = "black").grid(row=2,column=2)
    min_temp = json_data['main']['temp_min']-273.15
    print(min_temp)
    Label(root, text=round(min_temp,2), padx=12, font='Malgun 10 bold',bg = "turquoise1",fg = "black").grid(row=3, column=2)
    max_temp = json_data['main']['temp_max']-273.15
    Label(root, text=round(max_temp,2), padx=12, font='Malgun 10 bold',bg = "turquoise1",fg = "black").grid(row=4, column=2)
    Humidity = json_data['main']['humidity']
    Label(root, text=round(Humidity,2), padx=14, font='Malgun 10 bold',bg = "turquoise1",fg = "black").grid(row=5, column=2,padx=14)

    pressure  = json_data['main']['pressure']
    Label(root, text=pressure, padx=12, font='Malgun 10 bold',bg = "turquoise1",fg = "black").grid(row=6, column=2)
    windspeed = round(json_data['wind']['speed']*3.48)

    Label(root, text =f'{windspeed}/km/h',padx=12, font='Malgun 10 bold',bg = "turquoise1",fg = "black").grid(row=7, column=2)

    Today = json_data['weather'][0]['description'].capitalize()
    # Label(root, text=f"Todays weather is {Today}", padx=12, font='Malgun 10 bold').grid(row=5, column=3)
    if Today == 'Mist':
        Today= 'Fogy'
    tmsg.showinfo("Weather_Info", f"Today weather is {Today}")

now = datetime.now()
today = date.today()
# print("DATE:", today)
# print("TIME : ",datetime.now().time())
Label(root,text  = now,relief  =SUNKEN,font = 'mv 10 bold ', bd =5,bg='grey',fg='black').grid(row=10,column=3)

root.configure(bg = '#49A')
Label(root,text = "WEATHER TODAY", font = 'mv 10 bold ',padx = 20,pady=5,relief  =SUNKEN,bg ="grey",bd=4).grid(row=0,column=1,padx=20,pady=10)

Label(root,text = "CITY",font ='Cambria',padx = 20,bg = 'grey',fg = 'black',bd = 5,relief = SUNKEN).grid(row = 0,column = 2,padx=20,pady=10)
Label(root,text = "Temperature",font ='Cambria',padx = 45,relief  =SUNKEN,bd =5,bg ='LightPink1').grid(row = 2,column =1,padx=20,pady=10)
Label(root,text = "MAXIMUM Temperature",font ='Cambria',padx = 10,relief  =SUNKEN,bd =5,bg ='LightPink1').grid(row = 3,column =1,padx=20,pady=10)
Label(root,text = "MINIMUM Temperature",font ='Cambria',padx = 12,relief  =SUNKEN,bd =5,bg ='LightPink1').grid(row = 4,column =1,padx=20,pady=10)
Label(root,text = "HUMIDITY",font ='Cambria',padx = 60,relief  =SUNKEN,bd =5,bg ='LightPink1').grid(row = 5,column =1,padx=20,pady=10)
Label(root,text = "PRESSURE",font ='Cambria',padx = 60,relief  =SUNKEN,bd =5,bg ='LightPink1').grid(row = 6,column =1,padx=20,pady=10)
Label(root,text = "WINDSPEED",font ='Cambria',padx = 60,relief  =SUNKEN,bd =5,bg ='LightPink1').grid(row = 7,column =1,padx=20,pady=10)


city_value = StringVar()
cityentry = Entry(root, textvariable = city_value,bd = 5).grid(row =0,column=3,padx = 5,pady = 60)


Button(root,text = "OK",fg = "black",bg="grey",font = 'bold',padx = 5,pady = 1,relief=RAISED,command = order,borderwidth=8).grid(row = 0,column=5,padx = 3)

Button(root, text="QUIT", command=root.destroy,relief = RAISED,bd =4,bg = "grey").grid(row = 11,column = 2)

# root.wm_iconbitmap("Oxygen-Icons.org-Oxygen-Status-weather-clouds.ico")
# my_pic = Image.open("Status-weather-clouds-icon.png")
# resized = my_pic.resize((45,45),Image.ANTIALIAS)
# new_pic = ImageTk.PhotoImage(resized)
# my_pic = ImageTk.PhotoImage(file = "Status-weather-clouds-icon.png")
# pic_label = Label(root,image = new_pic,)
# pic_label.grid(row = 0,column=0)

Label(root,text = "Developer : Ajay Kumar",bg = "grey",font = 'Aestheticism 9 bold').grid(row=12,column = 3)
root.mainloop()