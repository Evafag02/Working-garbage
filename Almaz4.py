from tkinter import *
import random

def calculation():

    size = int(a.get())
    temps = [random.randint(-10, 10) for i in range(size)]
    avg = 0
    for i in temps:
        avg += i
    avg = avg / size
    e.set(str(avg))
def delete_all():
    a.set("")
    e.set("")

root = Tk()
root.title("file.py")
root.geometry("400x150")

a = StringVar()
e = StringVar()
Label(root, text="enter the size of the array: ").place(x=115, y=10)
Entry(root, textvariable=a).place(x=115, y=30)
Label(root, text="average temp:").place(x=115, y=70)
Entry(root, textvariable=e).place(x=115, y=90)

but = Button(text="Посчитать", command=calculation).place(x=100, y=120)
but2 = Button(text='Очистить', command=delete_all).place(x=200, y=120)

root.mainloop()