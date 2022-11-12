import tkinter

window = tkinter.Tk()
window.title("CobaLabel")
window.geometry('600x100')

#membuat label
Label1 = tkinter.Label(window, text="my first texy", font=15, bg="green", fg="white").pack()
Label1 = tkinter.Label(window, text="   Universitas Sulawesi Barat", font=15,  fg="white").pack()


window.mainloop()

