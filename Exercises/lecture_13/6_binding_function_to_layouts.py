from tkinter import *
from tkinter import ttk  # themed tk

root = Tk()


def print_name():
    print('hello')

# 'command' input - which function to bind to widget
button1 = Button(root, text='print', command=print_name).pack()


def print_numbers(event):
    print("1, 2, 3")

# 'bind' method - bind event on widget to function
button2 = Button(root, text='print 2')
button2.bind('<Button-1>', print_numbers)  # '<Button-1>' means left mouse click
button2.pack()

root.mainloop()
