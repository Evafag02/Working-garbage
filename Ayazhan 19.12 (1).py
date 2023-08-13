from tkinter import *

def calculation():
    n = int(a.get())
    m = int(b.get())
    e.set(power_of(n,m))

def power_of(n,m):
    return n**m

def delete_all():
    a.set("")
    b.set("")
    e.set("")

root = Tk()
root.title("1")
root.geometry("400x200")

a = StringVar()
b = StringVar()
e = StringVar()
Label(root, text="enter a num:").place(x=115, y=10)
Entry(root, textvariable=a).place(x=115, y=30)
Label(root, text="power of num:").place(x=115, y=50)
Entry(root, textvariable=b).place(x=115, y=70)
Label(root, text="result").place(x=115, y=90)
Entry(root, textvariable=e).place(x=115, y=110)

but = Button(text="Посчитать", command=calculation).place(x=100, y=130)
but2 = Button(text='Очистить', command=delete_all).place(x=200, y=130)

root.mainloop()