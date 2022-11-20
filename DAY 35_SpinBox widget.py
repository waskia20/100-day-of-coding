import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("CobaSpinBox")
window.geometry('600x300')

#membuatSpinBox
spin = Spinbox(window, from_ =0, to=50).pack()
window.mainloop()
