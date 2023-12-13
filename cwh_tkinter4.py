from tkinter import *

root = Tk()

# root.geometry("655x333")
# f1 = Frame(root, bg="grey", borderwidth=6)
# f1.pack(side=LEFT)

# # padx, pady, fillx, filly, etc.

# l = Label(f1, text = "Project Tkinter")
# l.pack()

root.geometry("655x333")
f1 = Frame(root, bg="grey", borderwidth=6, relief = SUNKEN)
f1.pack(side=LEFT, fill = "y")

# padx, pady, fillx, filly, etc.

f2 = Frame(root, borderwidth = 8, bg = "grey", relief = SUNKEN)
f2.pack(side = TOP, fill = "x")
l = Label(f1, text = "Project Tkinter - VSCode")
l.pack()
l = Label(f2, text = "Welcome to VSCode", font = "Helvetica 16 bold", fg = "red", pady = 10)
l.pack()


root.mainloop()