from tkinter import *
from tkinter import ttk  # themed tk
import tkinter.messagebox as msgbox

root = Tk()

root.title = 'Feet to Meters'
sw = root.winfo_screenwidth()  # get screen width in pixels
sh = root.winfo_screenheight()  # get screen size in pixels
winw = 300
winh = 100
gm = "{}x{}+{}+{}".format(winw, winh, sw//2-winw//2, sh//2-winh//2)
root.geometry(gm)

feet_str = DoubleVar()
meter_str = DoubleVar()

entry1 = Entry(root, textvariable=feet_str).grid(row=0, column=1)
label1 = Label(root, text='feet').grid(row=0, column=2)
label2 = Label(root, text='is equivalent to').grid(row=1, column=0)
label3 = Label(root, textvariable=meter_str).grid(row=1, column=1)
label4 = Label(root, text='meters').grid(row=1, column=2)
button1 = Button(root, text='Calculate')


def calc(event):
    try:
        feet = feet_str.get()
        meters = round(feet * 0.3048, 2)
        meter_str.set(meters)
    except:
        button1.config(relief=RAISED)
        msgbox.showerror('Error', 'Input is not a number, try again')

button1.bind("<Button-1>", calc)
button1.grid(row=2, column=2)

root.mainloop()

# tkinter error message:
# https://www.tutorialspoint.com/python/tk_messagebox.htm
# tkMessageBox.FunctionName(title, message [, options])