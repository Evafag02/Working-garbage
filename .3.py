from tkinter import *
import random

def calculation():
    n = int(a.get())
    list = []
    for i in range(n):
        list.append(random.randint(-20, 50))
    b.set(list)
    list2 = list[list.index(min(list)) + 1:]
    list = list[:list.index(min(list))]
    list.sort(reverse=True)
    list.extend(list2)
    e.set(list)


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
Label(root, text="enter an integer from:").place(x=145, y=10)
Entry(root, textvariable=a).place(x=115, y=30, width=180, height=20)
Label(root, text="list").place(x=50, y=70)
Entry(root, textvariable=b).place(x=115, y=70, width=180, height=20)
Label(root, text="reverse and sort list").place(x=10, y=90)
Entry(root, textvariable=e).place(x=115, y=90, width=180, height=20)

but = Button(text="Посчитать", command=calculation).place(x=100, y=120)
but2 = Button(text='Очистить', command=delete_all).place(x=200, y=120)

root.mainloop()