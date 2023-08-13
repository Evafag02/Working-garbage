from tkinter import *

def calculation():
    a_list = list(map(int,a.get().strip().split()))
    b_list = a_list[a_list.index((min(a_list))):]
    b_list.remove(min(a_list))
    e.set(b_list)

def delete_all():
    a.set("")
    e.set("")

root = Tk()
root.title("1")
root.geometry("400x200")

a = StringVar()
e = StringVar()
Label(root, text="enter a list:").place(x=115, y=10)
Entry(root, textvariable=a).place(x=115, y=30)
Label(root, text="result").place(x=115, y=50)
Entry(root, textvariable=e).place(x=115, y=70)

but = Button(text="Посчитать", command=calculation).place(x=100, y=100)
but2 = Button(text='Очистить', command=delete_all).place(x=200, y=100)

root.mainloop()