import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Sapa Dia!")

NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

#frame input
input_frame = ttk.Frame(window)

#penempatan Grid,pack,place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

#komponen-komponen
#1.label nama depan
nama_depan_Label = ttk.Label(input_frame,text="Nama Depan:")
nama_depan_Label.pack(padx=10,fill="x",expand=True)

#2.entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)

#3.label nama belakang
nama_belakang_Label = ttk.Label(input_frame,text="Nama Belakang:")
nama_belakang_Label.pack(padx=10,fill="x",expand=True)

#4.entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)

#5 tombol
def tombol_click():
    '''funsi ini akan dipanggil oleh tombol'''
    pesan=f"hallo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()},Cantik manisss,tetap semangat yah dan ingat orang tua!"
    showinfo(title="hi",message=pesan)
tombol_sapa = ttk.Button(input_frame,text="sapa!",command=tombol_click)
tombol_sapa.pack(fill='x',expand=True,padx=10,pady=10)

window.mainloop()
