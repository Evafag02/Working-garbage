from tkinter import *

def calculation():
    dist = float(a.get())
    gas = float(b.get())
    price = float(c.get())
    res=dist*2*gas/100*price
    e.set(res)

def delete_all():
    b.set("")
    a.set("")
    c.set("")
    e.set("")

root = Tk()
root.title("file.py")
root.geometry("400x150")

a = StringVar()
b = StringVar()
c = StringVar()
e = StringVar()
Label(root, text="distance to the cottage").place(x=50, y=10)
Label(root, text="gasoline consumptione").place(x=50, y=30)
Label(root, text="price of a liter of gas (tg)").place(x=50, y=50)
Entry(root, textvariable=a).place(x=200, y=10)
Entry(root, textvariable=b).place(x=200, y=30)
Entry(root, textvariable=c).place(x=200, y=50)
Label(root, text="res").place(x=50, y=90)
Entry(root, textvariable=e).place(x=200, y=90)

but = Button(text="Посчитать", command=calculation).place(x=100, y=120)
but2 = Button(text='Очистить', command=delete_all).place(x=200, y=120)

root.mainloop()
