from tkinter import *

def calculation():
    n = int(a.get())
    largest = 0
    while (n):
        r = n % 10
        largest = max(r,largest)
        n //= 10
    e.set(largest)

def delete_all():
    a.set("")
    e.set("")

root = Tk()
root.title("file.py")
root.geometry("400x150")

a = StringVar()
e = StringVar()
Label(root, text="Enter a number").place(x=115, y=10)
Entry(root, textvariable=a).place(x=115, y=30)
Label(root, text="Result").place(x=115, y=50)
Entry(root, textvariable=e).place(x=115, y=70)

but = Button(text="Посчитать", command=calculation).place(x=100, y=100)
but2 = Button(text='Очистить', command=delete_all).place(x=200, y=100)

root.mainloop()