from tkinter import *

def calculation():
    n = int(a.get())
    list = []
    while n != 0:
        list.append(n % 10)
        n //= 10
    e.set(min(list))

def delete_all():
    a.set("")
    e.set("")

root = Tk()
root.title("file.py")
root.geometry("400x150")

a = StringVar()
e = StringVar()
Label(root, text="enter an integer from:").place(x=115, y=10)
Entry(root, textvariable=a).place(x=115, y=30)
Label(root, text="res").place(x=115, y=70)
Entry(root, textvariable=e).place(x=115, y=90)

but = Button(text="Посчитать", command=calculation).place(x=100, y=120)
but2 = Button(text='Очистить', command=delete_all).place(x=200, y=120)

root.mainloop()