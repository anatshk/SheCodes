from tkinter import *
from tkinter import ttk  # themed tk

root = Tk()

# different behavior on right, middle or left click


def left_click(event):
    print('left')


def middle_click(event):
    print('middle')


def right_click(event):
    print('right')

frame = Frame(root, width=300, height=250)  # invisible frame, but it has size, so it will adjust window size
# we need the frame to bind events - must have a widget to bind to
frame.bind('<Button-1>', left_click)
frame.bind('<Button-3>', right_click)
frame.bind('<Button-2>', middle_click)

# one widget can have multiple events!

frame.pack()

root.mainloop()