from tkinter import *
from tkinter import ttk  # themed tk

root = Tk()
ment = StringVar()  # define ment to be a string variable
# other options are IntVar, DoubleVar, BooleanVar


def foo():
    mtext = ment.get()  # get the value stored in ment
    label2 = Label(root, text=mtext).pack()  # create a new label with that text
    return

root.geometry('450x450+500+300')  # root window size (NxM pixels) and location on screen (+X+Y pixels)
root.title('This is a title')  # set title to gui

label1 = Label(root, text='My Label', fg='red', bg='white').pack()
button1 = Button(root, text='OK', command=foo, fg='red', bg='blue').pack()
entry1 = Entry(root, textvariable=ment).pack()  # link ment to entry1,
# whenever text is entered to entry1, it is stored in ment

# setting a default value to entry
default_text = StringVar()
default_text.set('blah')
entry2 = Entry(root, textvariable=default_text).pack()

root.mainloop()


# read more:
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/control-variables.html