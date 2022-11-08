from tkinter import *

root = Tk()

def pilih():
    pilihan = "kamu memilih pilihan"+ str(var.get())
    hasil.config(text=pilihan)

var = IntVar()
opsi1 =Radiobutton(root,text='pilihan1',variable=var, value=1,command=pilih)
opsi1.pack(anchor=W)

opsi2 =Radiobutton(root,text='pilihan2',variable=var, value=2,command=pilih)
opsi2.pack(anchor=W)

opsi3 =Radiobutton(root,text='pilihan3',variable=var, value=3,command=pilih)
opsi3.pack(anchor=W)

hasil = Label(root)
hasil.pack()

root.mainloop()


