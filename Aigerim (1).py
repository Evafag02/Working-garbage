from tkinter import *

def calculation():
    d = float(a.get())
    t = float(b.get())
    speed = round(((d/t)*3.6), 2)
    e.set(speed)
def delete_all():
    a.set("")
    b.set("")
    e.set("")

root = Tk()
root.title("file.py")
root.geometry("400x200")

a = StringVar()
b = StringVar()
e = StringVar()
Label(root, text="Distance? (in meters)").place(x=115, y=10)
Entry(root, textvariable=a).place(x=115, y=30)
Label(root, text="Time? (in seconds)").place(x=115, y=50)
Entry(root, textvariable=b).place(x=115, y=70)
Label(root, text="Result (km/h)").place(x=115, y=90)
Entry(root, textvariable=e).place(x=115, y=110)

but = Button(text="Посчитать", command=calculation).place(x=100, y=140)
but2 = Button(text='Очистить', command=delete_all).place(x=200, y=140)

root.mainloop()