from tkinter import *


class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Title
        Label(self, text='choose movie type').grid(row=0, column=0, sticky=W)

        # instructions
        Label(self, text='select all that apply:').grid(row=1, column=0, sticky=W)

        # check buttons
        self.comedy = BooleanVar()  # data of the checkbox
        Checkbutton(self, text='comedy', variable=self.comedy, command=self.update_text).grid(row=2, column=0, sticky=W)

        self.drama = BooleanVar()  # data of the checkbox
        Checkbutton(self, text='drama', variable=self.drama, command=self.update_text).grid(row=3, column=0, sticky=W)

        self.romance = BooleanVar()  # data of the checkbox
        Checkbutton(self, text='romance', variable=self.romance, command=self.update_text).grid(row=4, column=0, sticky=W)

        # result
        self.result = Text(self, width=40, height=5, wrap=WORD)  # wrappinf without cutting words
        self.result.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        """
        update and display movie types
        :return:
        """

        likes = ""  # initialize empty result

        # append all that marked as True
        if self.comedy.get():
            likes += 'comedy, '
        if self.drama.get():
            likes += 'drama, '
        if self.romance.get():
            likes += 'romance'

        self.result.delete(0.0, END)  # delete the current result value
        self.result.insert(0.0, likes)  # insert new result value

root = Tk()
root.title('Movie Genre')
app = App(root)
root.mainloop()