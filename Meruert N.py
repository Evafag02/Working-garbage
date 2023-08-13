from tkinter import *

def click1():
    n = int(input("Vvedite n-> "))
    number,sum = n, 0
    for i in range(n + 1):
        sum += i
         e.set(sum)

def click2():
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt1.focus()


window = Tk()
window.title("Week №10")
window.geometry("300x150")

lbl1 = Label(window, text="Enter n-> ")
lbl1.place(x=10, y=15)

txt1 = Entry(window, width=15)
txt1.place(x=85, y=19)

lbl2 = Label(window, text="Enter s-> ")
lbl2.place(x=10, y=50)

txt2 = Entry(window, width=15)
txt2.place(x=85, y=54)

btn1 = Button(window, text = "Run", command = click1)
btn1.place(x=60, y=100)

btn2 = Button(window, text = "Clear", command = click2)
btn2.place(x=200, y=100)

window.mainloop()

