
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("1255x944")
# photo = PhotoImage(file="photo.jpg")

#NOTE : tkinter doesn't support jpg images, hence we need to use PIL images

#For JPG images

image = Image.open("photo.jpg")
photo = ImageTk.PhotoImage(image)

label = Label(image=photo)
label.pack()

root.mainloop()
