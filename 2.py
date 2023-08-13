from tkinter import *

def calculation():
    x = float(a.get())
    if x >= 1 and x <=7:
        e.set('Asia')
        if x == 1:
            print("Asia")
        elif x == 2:
            e.set(" Africa")
        elif x == 3:
            e.set("North America")
        elif x == 4:
            e.set(" South America")
        elif x == 5:
            e.set(" Antarctica")
        elif x == 6:
            e.set("Europe")
        elif x == 7:
            e.set(" Australia")
    else:
        e.set("Enter number from 1 to 7")

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