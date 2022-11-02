import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("CobaPack")
window.geometry('600x100')

#membuat pack
Button1 = Button(window, text="left", bg="green").pack(side=LEFT, expand=YES, fill=Y)
Button2 = Button(window, text="Top", bg="red").pack(side=TOP, expand=YES, fill=BOTH)
Button2 = Button(window, text="Right", bg="blue").pack(side=LEFT, expand=YES, fill=X)
