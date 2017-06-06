from tkinter import *


class Window(Frame):
    # Frame is a tkinter class
    def __init__(self, master=None):
        Frame.__init__(self, master)  # init parent class
        self.master = master  # main window
        self.pack()  # pack the Window (which is a Frame)
        self.create_widgets()

    def create_widgets(self):
        """ Create buttons that do nothing at this point """
        self.button1 = Button(self, text='blah1')
        self.button1.grid()

        self.button2 = Button(self, text='blah2')
        self.button2.grid()

# start GUI - open an empty window
root = Tk()

app = Window(root)  # root goes as master

root.mainloop()
