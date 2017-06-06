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
        Label(self, text='select one:').grid(row=1, column=0, sticky=W)

        # variable for single movie type
        self.favorite = StringVar()

        # note that values need to be assigned to radio buttons
        Radiobutton(self, text='comedy', value='comedy', variable=self.favorite, command=self.update_text).grid(row=2, column=0, sticky=W)
        Radiobutton(self, text='drama', value='drama', variable=self.favorite, command=self.update_text).grid(row=3, column=0, sticky=W)
        Radiobutton(self, text='romcom', value='romcom', variable=self.favorite, command=self.update_text).grid(row=4, column=0, sticky=W)
        Radiobutton(self, text='romcom parodies', value='romcom', variable=self.favorite, command=self.update_text).grid(row=4, column=1, sticky=W)

        # Note: assigning the same value to 2 or more radio buttons links them - they are selected\deselected together

        # create another bank of buttons, assign a different variable to each group:
        self.favorite_2 = StringVar()
        Radiobutton(self, text='comedy2', value='comedy2', variable=self.favorite_2, command=self.update_text).grid(row=5,
                                                                                                                column=0,
                                                                                                                sticky=W)
        Radiobutton(self, text='drama2', value='drama2', variable=self.favorite_2, command=self.update_text).grid(row=6,
                                                                                                              column=0,
                                                                                                              sticky=W)
        # (these buttons don't change the text, they're just here to show

        self.result = Text(self, width=40, height=5, wrap=WORD)
        self.result.grid(row=10, column=0, columnspan=3)

    def update_text(self):
        """ update test area """

        msg = 'you selected: '
        msg += self.favorite.get()

        self.result.delete(0.0, END)  # delete the current result value
        self.result.insert(0.0, msg)  # insert new result value

root = Tk()
root.title('Movie Genre 2')
app = App(root)
root.mainloop()
