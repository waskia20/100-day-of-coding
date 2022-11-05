from tkinter import *

#membuat dengan menggunakan widget frame dan labelframe
root=Tk()
root.title("Frame ku")

#membuat frame pertama
f=Frame(root, cursor='dot', bg='red')
Label(f, text='ini merupakan program frame', fg='white', bg='red').pack()
Label(f, text='saya sedang belajar pemprograman python', fg='white', bg='red').pack()
Label(f, text='dalam bahasa pemprograman GUI tkinter', fg='white', bg='red').pack()
f.pack(expand=YES, fill=BOTH)

#membuat frame kedua
f2=LabelFrame(root, text='frame kedua ku', bd=8, bg='white')
Label(f2, text='ini frame kedua saya', fg='red', bg='white').pack()
Label(f2, text='menulis pada label frame', fg='red', bg='white').pack()
Label(f2, text='teks label frame yang ketiga', fg='red', bg='white').pack()
f2.pack(expand=YES, fill=BOTH)

mainloop()
