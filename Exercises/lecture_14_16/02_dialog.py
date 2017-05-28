from tkinter import *
from tkinter import messagebox

root = Tk()

# *********** Functions ***********


def about():
    messagebox.showinfo(title='About', message='blah blah')  # show info icon
    # messagebox.showwarning(title='About', message='blah blah')  # show warning icon
    # messagebox.showerror(title='About', message='blah blah')  # show error icon


def quit():
    exit = messagebox.askyesno(title='quit', message='are you sure?')
    if exit > 0:
        root.destroy()
        return


# *********** Main Menu ***********

menu = Menu(root)  # define a Menu object, put in in root window
root.config(menu=menu)  # configure the menu object

submenu = Menu(menu)  # create a submenu - this will drop down from main menu
menu.add_cascade(label='file', menu=submenu)
submenu.add_command(label='about', command=about)
submenu.add_command(label='exit', command=quit)

root.mainloop()
