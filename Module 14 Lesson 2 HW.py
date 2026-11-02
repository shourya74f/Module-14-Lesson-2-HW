from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window=Tk()
window.title("Photo Album")
window.geometry("800x600")

t=Label(window, text="Photo Album", fg="blue", bg="yellow")
t.pack(pady=15)

i=Image.open("images.jpeg")
p=ImageTk.PhotoImage(i)
il=Label(window, image=p)
il.pack(pady=15)

def sd():
    top=Toplevel(window)
    top.title("Show Details")
    top.geometry("400x300")
    d=Label(top, text="Details of the photo:\nLocation: New York\nDate: 2023-01-01", fg="blue", bg="yellow")
    d.pack(pady=15)
    
b=Button(window, text="Show Details",bg="lightgray", command=sd)
b.pack(pady=15)

window.mainloop()