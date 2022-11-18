import tkinter

window = tkinter.Tk()
window.title("CobaButton")
window.geometry('600x300')

#membuat button
tombol1= tkinter.Button(window,text="Home").pack()
tombol2= tkinter.Button(window, text="informasi").pack()

window.mainloop()
