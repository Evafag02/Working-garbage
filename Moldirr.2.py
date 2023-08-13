from tkinter import *

def calculation():
    z = str(a.get())
    z2 = str(b.get())
    y1 = [int(y) for y in z.split()]
    y2 = [int(y2) for y2 in z2.split()]
    y1_ans = []
    for i in y1:
        if 24 >= i >= 0:
            y1_ans.append(0)
        elif 49 >= i >= 25:
            y1_ans.append(0.5)
        elif 54 >= i >= 50:
            y1_ans.append(1)
        elif 59 >= i >= 55:
            y1_ans.append(1.33)
        elif 64 >= i >= 60:
            y1_ans.append(1.66)
        elif 69 >= i >= 65:
            y1_ans.append(2)
        elif 74 >= i >= 70:
            y1_ans.append(2.33)
        elif 79 >= i >= 75:
            y1_ans.append(2.67)
        elif 84 >= i >= 80:
            y1_ans.append(3)
        elif 89 >= i >= 85:
            y1_ans.append(3.33)
        elif 94 >= i >= 90:
            y1_ans.append(3.67)
        elif 100 >= i >= 95:
            y1_ans.append(4)
    x = sum(y1_ans)/sum(y2)
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