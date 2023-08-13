import math
from tkinter import *

def calculation():

    initial = deposit = int(a.get())
    percent = int(b.get()) / 100
    day = int(c.get())

    income = deposit * percent / 365

    e.set(income * day)
    g.set(math.ceil(initial + (income * day)))
def delete_all():
    a.set("")
    b.set("")
    c.set("")
    g.set("")
    e.set("")

root = Tk()
root.title("Week9")
root.geometry("400x300")

a = StringVar()
b = StringVar()
c = StringVar()
g = StringVar()
e = StringVar()
Label(root, text="Вклад").place(x=115, y=10)
Entry(root, textvariable=a).place(x=115, y=30)
Label(root, text="Годовой процент").place(x=115, y=50)
Entry(root, textvariable=b).place(x=115, y=70)
Label(root, text="Срок хранения (в дня)").place(x=115, y=90)
Entry(root, textvariable=c).place(x=115, y=110)
Label(root, text="Res: Income (tg)").place(x=115, y=130)
Entry(root, textvariable=e).place(x=115, y=150)
Label(root, text="Res: Amount at the end of the deposit term (tg)").place(x=115, y=170)
Entry(root, textvariable=g).place(x=115, y=190)

but = Button(text="Посчитать", command=calculation).place(x=100, y=220)
but2 = Button(text='Очистить', command=delete_all).place(x=200, y=220)

root.mainloop()