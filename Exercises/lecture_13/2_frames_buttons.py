from tkinter import *
from tkinter import ttk  # themed tk

# example on how to arrange layout:
root = Tk()  # creates a blank window

topFrame = Frame(root)  # creates a frame (a layout element, invisible rectangle where we can place widgets)
topFrame.pack()  # places frame in root window
bottomFrame = Frame(root)  # creates another frame
bottomFrame.pack(side=BOTTOM)  # places frame in root window, on the BOTTOM of the window
# 'side' is not provided in topFrame because as soon as bottomFrame is placed, the side of top is automatically assigned

button1 = Button(topFrame, text='Button 1', fg='red')  # create a button and place it in topFrame,
                                                       # specify text on the button and button color
button2 = Button(topFrame, text='Button 2', fg='blue')
button3 = Button(topFrame, text='Button 3', fg='green')
button4 = Button(bottomFrame, text='Button 4', fg='purple')  # this button goes into the bottom frame

# pack the buttons into the root window
button1.pack(side=LEFT)  # pack this button as far to the left as possible
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)  # button4 is the only item in bottom frame so specifying side is redundant,
                           # regardless of side value, the button will be in the middle of the frame
root.mainloop()   # keeps the gui running (uncomment to see gui)