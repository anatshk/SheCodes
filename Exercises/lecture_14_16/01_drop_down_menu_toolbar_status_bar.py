from tkinter import *


# this is a function that defines what happens when we click a menu item on the drop down menu
# it does nothing in this case
def do_nothing():
    print('blah')

# in the example below, all commands use 'do_nothing' - but they should point to different functions

root = Tk()

# *********** Main Menu ***********

menu = Menu(root)  # define a Menu object, put in in root window
root.config(menu=menu)  # configure the menu object

submenu = Menu(menu)  # create a submenu - this will drop down drom main menu
menu.add_cascade(label='file', menu=submenu)  # when we click 'file' on the main menu, then 'submenu' will open
submenu.add_command(label='new...', command=do_nothing)  # we've added an item to our dropdown menu,
                                                         # command defines what will happen when we select this item
submenu.add_command(label='blah', command=do_nothing)  # another item
submenu.add_separator()  # adds a horizontal line in drop down menu
submenu.add_command(label='exit', command=do_nothing)  # another item

submenu2 = Menu(menu)  # another dropdown menu
menu.add_cascade(label='edit', menu=submenu2)
submenu2.add_command(label='redo', command=do_nothing)

# *********** Toolbar ***********

toolbar = Frame(root, bg='blue')  # create a frame in the bottom of the window (color for example only)
insert_button = Button(toolbar, text='insert image', command=do_nothing)  # button on the toolbar
insert_button.pack(side=LEFT, padx=2, pady=2)  # put button in left of frame, pad with 2 piels
print_button = Button(toolbar, text='print', command=do_nothing)
print_button.pack(side=LEFT, padx=2, pady=2)  # put button in left of frame, pad with 2 piels

toolbar.pack(side=TOP, fill=X)  # main menu is automatically at top, so this will be just below

# *********** Status Bar ***********

status = Label(root, text='this is the status', bd=1, relief=SUNKEN, anchor=W)
# bd is border, relief is 3D feature - sunken \ raised, anchor - aligns text
status.pack(side=BOTTOM, fill=X)

# the text in the status bar can be changed depending on what the mouse hovers on.

root.mainloop()
