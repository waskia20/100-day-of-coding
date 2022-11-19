import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("CobaRadioButton")
window.geometry('600x300')

#membuatRadiobutton
Radiob1 = Radiobutton(window, text="Teknik Informatika", value=1).pack()
Radiob2 = Radiobutton(window, text="Sistem Informasi", value=2).pack()

window.mainloop()
