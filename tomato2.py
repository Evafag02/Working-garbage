
from tkinter import *

def calculation():
    y = float(a.get())
    z = float(b.get())
    x = float(c.get())
    S = float(2*(y*z+z*x+x*y))
    e.set(S)
def delete_all():
    a.set("")
    b.set("")
    c.set("")
    e.set("")

root = Tk()
root.title("Lab13")
root.geometry("400x250")

a = StringVar()
b = StringVar()
c = StringVar()
e = StringVar()
Label(root, text="Length (cm):").place(x=115, y=10)
Entry(root, textvariable=a).place(x=115, y=30)
Label(root, text="Width (cm):").place(x=115, y=50)
Entry(root, textvariable=b).place(x=115, y=70)
Label(root, text="Height (cm):").place(x=115, y=90)
Entry(root, textvariable=c).place(x=115, y=110)
Label(root, text="Surface area (sq.cm):").place(x=115, y=130)
Entry(root, textvariable=e).place(x=115, y=150)

but = Button(text="Посчитать", command=calculation).place(x=100, y=180)
but2 = Button(text='Очистить', command=delete_all).place(x=200, y=180)

root.mainloop()