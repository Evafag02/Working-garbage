from tkinter import *

def EKOE(a,b):
    e.set(a*b)
def calculation():
    x,y = float(a.get()), float(b.get())
    EKOE(x,y)
def delete_all():
    a.set("")
    b.set("")
    e.set("")

root = Tk()
root.title("file.py")
root.geometry("400x200")

a = StringVar()
b = StringVar()
e = StringVar()
Label(root, text="M").place(x=115, y=10)
Entry(root, textvariable=a).place(x=115, y=30)
Label(root, text="N").place(x=115, y=50)
Entry(root, textvariable=b).place(x=115, y=70)
Label(root, text="Result").place(x=115, y=90)
Entry(root, textvariable=e).place(x=115, y=110)

but = Button(text="Посчитать", command=calculation).place(x=100, y=140)
but2 = Button(text='Очистить', command=delete_all).place(x=200, y=140)

root.mainloop()