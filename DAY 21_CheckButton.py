from tkinter import *

root = Tk()
root.title("checkbutton")

r = IntVar()
r2 = IntVar()

chek = Checkbutton(root,text="nomor 1",variable=r,onvalue=1,offvalue=0)
chek.grid()
chek2 = Checkbutton(root,text="nomor 2",variable=r2,onvalue=1,offvalue=0)
chek2.grid()

def cetak():
    satu =r.get()
    dua =r2.get()
    if satu == 1 and dua == 0:
        Label(root,text ="no satu saja").grid()
    elif dua == 1 and satu == 0:
        Label(root,text ="no dua saja").grid()
    elif satu == 1 and dua == 1:
        Label(root,text ="satu dan dua").grid()
    elif satu == 0 and dua == 0:
        Label(root,text ="tidak milih ").grid()
    
btn = Button(root,text="submit",command=cetak)
btn.grid()
root.mainloop()
    

    
