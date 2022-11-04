#membuat button
import tkinter
from tkinter import *
syp = tkinter.Tk()
syp.title('membuat Button')
syp.geometry('1000x400')

def mahasiswa():
    print("yok bisa yok :)")

btn = Button(syp, text="Halo semuanya", fg="#000000", padx=12, pady=12,command=mahasiswa)
btn.pack()
syp.mainloop()
