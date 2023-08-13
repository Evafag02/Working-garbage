from tkinter import *

def calculation():
    scale = float(a.get())
    distance = float(b.get())
    res = scale * distance
    e.set(res)
def delete_all():
    a.set("")
    e.set("")

root = Tk()
root.title("file.py")
root.geometry("250x200")

a = StringVar()
b = StringVar()
e = StringVar()
Label(root, text="Scale:").place(x=70, y=10)
Entry(root, textvariable=b).place(x=70, y=30)
Label(root, text="Distance:").place(x=70, y=50)
Entry(root, textvariable=a).place(x=70, y=70)
Label(root, text="Res:").place(x=70, y=90)
Entry(root, textvariable=e).place(x=70, y=110)

but = Button(text="Calculate", command=calculation).place(x=70, y=140)
but2 = Button(text='Clear', command=delete_all).place(x=150, y=140)

root.mainloop()