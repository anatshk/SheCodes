from tkinter import *
from tkinter import ttk  # themed tk

root3 = Tk()

root3.geometry('450x450+500+300')  # root window size (NxM pixels) and location on screen (+X+Y pixels)
root3.title('This is a title')  # set title to gui
label1 = Label(root3, text='This is a label', fg='red', bg='blue').place(x=225, y=225)  # place label at specific location
# coordinates are from top left corner of GUI
label2 = Label(root3, text='this is another label', fg='blue', bg='yellow').grid(row=0, column=0)
label3 = Label(root3, text='this is a third, longer, label', fg='yellow', bg='black').grid(row=1, column=0)
# notice that the grid changes shape - now both labels 2 and 3 are in column 1, and the column is wider to fit label 3
# we can shift the labels within the grid to left\right of column using N, S, E, W (compass) directions
label4 = Label(root3, text='label 4', fg='black', bg='red').grid(row=2, column=0, sticky=W)
label5 = Label(root3, text='very very very very very long label 5', fg='blue', bg='pink').grid(row=0, column=1)
# label 5 is in the 2nd column - note that it starts where label 3 ends

# NOTE: if geometry is not provided - window is going to be minimum size to fit all items
# (comment root3.geometry for example)

"""
pack() - places in the center of screen
place() - uses x, y coordinates in pixels
grid() - uses row\column grid with varying column width
"""

root3.mainloop()