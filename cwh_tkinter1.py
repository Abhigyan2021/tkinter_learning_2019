
from tkinter import *

_root = Tk()

# Width x Height
_root.geometry("644x434")

# width, height
_root.minsize(400,300)

# width, height
_root.maxsize(700, 600)

eddy = Label(text="Eddy is Awesome and this is his GUI.")
eddy.pack()

_root.mainloop()


