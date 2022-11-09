from tkinter import *
root = Tk()
scale = Scale(root,from_=0, to=100, orien=HORIZONTAL)
scale.set(20)
scale.pack()
root.mainloop()
