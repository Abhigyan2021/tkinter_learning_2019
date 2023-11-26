from tkinter import *
root = Tk()
root.geometry("444x333")
root.title("My GUI with Harry")


'''
Important Label Options:

text = adds the text
bd = background
fg = foreground
font - sets the font

1. font = ("comicsansms", 19, "bold")
2. font = "comicsansms 19 bold"

padx = x padding
pady = y padding
relief = border styling(SUNKEN, RAISED, GROOVE, RIDGE)

'''

title_label = Label(text = '''Abdul Rashid Salim Salman Khan is an Indian actor, film producer, and television personality who works predominantly in Hindi films. \nIn a career spanning over three decades, Khan has received numerous awards, including two National Film Awards as a film producer, and a Filmfare Award as an actor.\n He is cited in the media as one of the most commercially successful actors of Indian cinema.\nForbes has included Khan in listings of the highest-paid celebrities in the world, in 2015 and 2018, with him being the highest-ranked Indian in the latter year.\n

Khan began his acting career with a supporting role in Biwi Ho To Aisi (1988), followed by his breakthrough with a leading role in Sooraj Barjatya's romance Maine Pyar Kiya (1989). \nHe established himself in the 1990s, with several commercially successful films, including Barjatya's family dramas Hum Aapke Hain Koun..! (1994) and Hum Saath-Saath Hain (1999), the action film Karan Arjun (1995) and the comedy Biwi No.1 (1999). 

''',
bg = "violet", fg = "white", padx= 30, pady = 30, font = "comicsansms 19 bold", borderwidth = 3, relief = SUNKEN

)


title_label.pack()

root.mainloop()