from tkinter import *
root = Tk()
scale = Scale(root,from_=0, to=100, orien=VERTICAL)
scale.set(22)
scale.pack()
root.mainloop()
