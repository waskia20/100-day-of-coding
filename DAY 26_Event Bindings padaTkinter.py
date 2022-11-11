import tkinter


window = tkinter.Tk()
window.title("coba")
window.geometry('600x100')

#creating a funtion called say Hello
def say_hello():
    tkinter.Label(window, text="Hello").pack()
tkinter.Button(window, text ="Click me!", command = say_hello).pack()

window.mainloop()
