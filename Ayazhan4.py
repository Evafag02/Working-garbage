from tkinter import *

def calculation():
    n = int(a.get())
    e.set(S(n))
def S(n):
    B = 2
    S = 1
    j = 3
    for i in range(n - 1):
        if B % 2 == 0:
            S += 1 / j
        else:
            S -= 1 / j
        B += 1
        j += 2
    return S

def delete_all():
    a.set("")
    e.set("")

root = Tk()
root.title("Week12")
root.geometry("400x150")

a = StringVar()
e = StringVar()
Label(root, text="enter a value:").place(x=115, y=10)
Entry(root, textvariable=a).place(x=115, y=30)
Label(root, text="res").place(x=115, y=70)
Entry(root, textvariable=e).place(x=115, y=90)

but = Button(text="Посчитать", command=calculation).place(x=100, y=120)
but2 = Button(text='Очистить', command=delete_all).place(x=200, y=120)

root.mainloop()