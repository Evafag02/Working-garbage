from tkinter import *

def calculation():
    san = int(a.get())
    sum = 1 / 2
    _ = 1
    l = 4
    for i in range(san - 1):
        if _ % 2 == 0:
            sum = sum - 1 / l
        else:
            sum = sum + 1 / l
        _ += 1
        l += 2
    e.set(sum)


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