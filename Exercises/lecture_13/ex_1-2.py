from tkinter import *
from tkinter import ttk  # themed tk

root = Tk()

root.title("Hello")  # set title to window

sw = root.winfo_screenwidth()  # get screen width in pixels
sh = root.winfo_screenheight()  # get screen size in pixels

# calculate window size from screen size
winw = 500
winh = 500

gm = "{}x{}+{}+{}".format(winw, winh, sw//2-winw//2, sh//2-winh//2)
root.geometry(gm)
# root.geometry("500x500+50+300")  # set window size (WxH) and location (+X+Y)

root.mainloop()
