from tkinter import *

def calculation():
    n = int(a.get())
    m = 1
    znak = 1
    for i in range(3,n+1,2):
        v = 1/i * znak
        znak = znak * (-1)
        m = m+v
        e.set(m)
def delete_all():
    a.set("")
    e.set("")

root = Tk()
root.title("Week11")
root.geometry("400x150")

a = StringVar()
e = StringVar()
Label(root, text="enter a value:").place(x=115, y=10)
Entry(root, textvariable=a).place(x=115, y=30)
Label(root, text="res").place(x=115, y=70)
Entry(root, textvariable=e).place(x=115, y=90)

but = Button(text="Посчитать", command=calculation).place(x=100, y=120)
but2 = Button(text='Очистить', command=delete_all).place(x=200, y=120)

root.mainloop()