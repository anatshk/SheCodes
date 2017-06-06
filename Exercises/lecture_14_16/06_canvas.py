from tkinter import *

root = Tk()
root.geometry("450x600+300+100")
root.title('blah')

# Canvas - a frame we can draw on. The default canvas color is same as background, so we set bg to make is visible.
canvas_1 = Canvas(root, height=300, width=300, bg='white')  # we can use hexadecimal values of colors WITHOUT QUOTES

# create objects on canvas (x1, y1, x2, y2)
canvas_1.create_line(0.0, 0.0, 300.0, 300.0)
canvas_1.create_oval(50, 150, 200, 250)  # x1, y1 and x2, y2 refer to the horizontal \ vertical axes of the oval
canvas_1.create_oval(150, 200, 200, 250)
canvas_1.create_rectangle(50, 100, 150, 200)  # 2 opposite corners of rectangle (top left, bottom right)

canvas_1.grid(row=0, column=0)  # we first must draw objects on canvas and then pack it


# arc
canvas_2 = Canvas(root, height=100, width=100, bg='blue')
coord = (10, 50, 90, 80)
arc = canvas_2.create_arc(coord, start=0, extent=110, fill='red')
# start and extent are in degrees, arc will be from start to start+extent degrees
canvas_2.grid(row=1, column=0)

root.mainloop()
