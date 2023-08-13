import math
import random
from tkinter import *

def calculation():
    a.set(math.pi)
    R1 = random.randrange(2, 10)
    R2 = random.randrange(1, R1)
    b.set(R1)
    c.set(R2)
    S1 = math.pi * R1 ** 2
    S2 = math.pi * R2 ** 2
    S3 = S1 - S2
    g.set(S1)
    e.set(S2)
    f.set(S3)
def delete_all():
    a.set("")
    b.set("")
    c.set("")
    g.set("")
    e.set("")
    f.set("")

root = Tk()
root.title("Week10")
root.geometry("400x300")

a = StringVar()
b = StringVar()
c = StringVar()
g = StringVar()
e = StringVar()
f = StringVar()

Label(root, text="Пи").place(x=115, y=10)
Entry(root, textvariable=a).place(x=115, y=30)
Label(root, text="Радиус 1").place(x=115, y=50)
Entry(root, textvariable=b).place(x=115, y=70)
Label(root, text="Радиус 2").place(x=115, y=90)
Entry(root, textvariable=c).place(x=115, y=110)
Label(root, text="Площадь круга 1").place(x=115, y=130)
Entry(root, textvariable=e).place(x=115, y=150)
Label(root, text="Площадь круга 2").place(x=115, y=170)
Entry(root, textvariable=g).place(x=115, y=190)
Label(root, text="Площадь кольца").place(x=115, y=210)
Entry(root, textvariable=g).place(x=115, y=230)

but = Button(text="Посчитать", command=calculation).place(x=100, y=260)
but2 = Button(text='Очистить', command=delete_all).place(x=200, y=260)

root.mainloop()