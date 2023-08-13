import random
from tkinter import *

def calculation():
    list = []
    n = int(a.get())
    m = int(b.get())
    for i in range(n):
        list.append(random.randint(-20, 20))

    c.set(list)

    if m in list:
        e.set(f"Да, число есть, его индекс: {list.index(m)}")
    else:
        e.set("Числа нет в списке")
def delete_all():
    a.set("")
    b.set("")
    e.set("")

root = Tk()
root.title("file.py")
root.geometry("400x150")

a = StringVar()
b = StringVar()
e = StringVar()
c = StringVar()
Label(root, text="enter an integer from:").place(x=115, y=10)
Entry(root, textvariable=a).place(x=115, y=30, width=180, height=20)
Entry(root, textvariable=b).place(x=115, y=50, width=180, height=20)
Label(root, text="list").place(x=80, y=70)
Entry(root, textvariable=c).place(x=115, y=70, width=180, height=20)
Label(root, text="res").place(x=80, y=90)
Entry(root, textvariable=e).place(x=115, y=90, width=180, height=20)

but = Button(text="Посчитать", command=calculation).place(x=100, y=120)
but2 = Button(text='Очистить', command=delete_all).place(x=200, y=120)

root.mainloop()