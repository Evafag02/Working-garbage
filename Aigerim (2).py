from tkinter import *

def calculation():
    b = a.get()
    if b[::-1] == b: e.set("palindrome")
    else: e.set('Is not a palindrome')

def delete_all():
    a.set("")
    e.set("")

root = Tk()
root.title("file.py")
root.geometry("400x200")

a = StringVar()
e = StringVar()
Label(root, text="enter a four-digit number").place(x=115, y=10)
Entry(root, textvariable=a).place(x=115, y=30)
Label(root, text="Result").place(x=115, y=90)
Entry(root, textvariable=e).place(x=115, y=110)

but = Button(text="Посчитать", command=calculation).place(x=100, y=140)
but2 = Button(text='Очистить', command=delete_all).place(x=200, y=140)

root.mainloop()