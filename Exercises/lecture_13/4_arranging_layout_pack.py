from tkinter import *
from tkinter import ttk  # themed tk

root = Tk()

one = Label(text='One', bg='red', fg='white').pack()  # standard packing
two = Label(text='Two', bg='green', fg='black').pack(fill=X)  # this label will be resized with the window WIDTH
three = Label(text='Three', bg='black', fg='blue').pack(side=LEFT, fill=Y)  # this label will be resized with the window HEIGHT

# change window size to see how 'one' stays the same, 'two' widens and 'three' grows in height

root.mainloop()
