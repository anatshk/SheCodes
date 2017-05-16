from tkinter import *
from tkinter import ttk  # themed tk

root = Tk()

label1 = Label(root, text='name')
label2 = Label(root, text='password')
entry1 = Entry(root)  # empty widget to enter test
entry2 = Entry(root)

# arrange according to grid, right-align labels
label1.grid(row=0, sticky=E)  # column is 0 by default
label2.grid(row=1, sticky=E)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

c = Checkbutton(root, text='keep me logged in')
c.grid(columnspan=2)  # columnspan specifies how many columns are used by the item

root.mainloop()
