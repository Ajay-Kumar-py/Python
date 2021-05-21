

import pywhatkit as kit
from tkinter import *


root = Tk()

root.geometry("245x135")
root.title("Song selection ")
frame=Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=5, width=100, height=100, bd= 0)
bgImage = PhotoImage(file = r'C:\Users\ajay.kumar\PycharmProjects\untitled\corrrrona.png')
Label(root, image = bgImage).place(relwidth=1, relheight = 1)

def order():

    sn = song_name.get()
    kit.playonyt(sn)


Button(root,text = "Search",fg = "black",bg="grey",font = 'bold',padx = 5,pady = 1,relief=RAISED,command = order,borderwidth=5).grid(row = 0,column=5,padx = 3)
song_name = StringVar()
song_entry = Entry(root, textvariable = song_name,bd = 5).grid(row =0,column=3,padx = 5,pady = 60)


root.mainloop()
