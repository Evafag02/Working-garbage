from tkinter import *

def calculation():
    z = str(a.get())
    z2 = str(b.get())
    y = [float(y) for y in z.split()]
    y2 = [float(y2) for y2 in z2.split()]
    x = sum(y)/sum(y2)
    e.set(x)

def delete_all():
    a.set("")
    e.set("")

root = Tk()
root.title("file.py")
root.geometry("250x200")

a = StringVar()
b = StringVar()
e = StringVar()
Label(root, text="Enter your credit:").place(x=70, y=10)
Entry(root, textvariable=b).place(x=70, y=30)
Label(root, text="Enter your mark:").place(x=70, y=50)
Entry(root, textvariable=a).place(x=70, y=70)
Label(root, text="Your GPA is:").place(x=70, y=90)
Entry(root, textvariable=e).place(x=70, y=110)

but = Button(text="Calculate", command=calculation).place(x=70, y=140)
but2 = Button(text='Clear', command=delete_all).place(x=150, y=140)

root.mainloop()