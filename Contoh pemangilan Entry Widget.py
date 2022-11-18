import tkinter

window = tkinter.Tk()
window.title("CobaEntry")
window.geometry('600x300')

#membuatEntry
Entry1 = tkinter.Entry(window, bg="green",fg="white").pack()
Entry2 = tkinter.Entry(window).pack()

window.mainloop()
