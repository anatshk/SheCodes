from tkinter import *
from tkinter import ttk  # themed tk
root = Tk()  # creates a blank window

# code for widgets goes here

# widgets are visual elements, buttons, menus, etc
# widgets have attributes - colors, fonts, etc.

lab = Label(root, text='blah')  # place text in the window. root - where to put the text
lab.pack()  # indicates that we want to put the text anywhere in the 'root' window, "just pack it in there"
root.mainloop()  # keeps the gui running (uncomment to see gui)
