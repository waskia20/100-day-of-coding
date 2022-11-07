from tkinter import *

top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'python')
Lb.insert(2, 'java')
Lb.insert(3, 'php')
Lb.insert(4, 'javascript')
Lb.pack()
top.mainloop()
