from tkinter import *

def loadedWithValueReturns(n):
  res=""
  for i in range(1,n+1,1):
    if(n % i==0):
      res=res+str(i)+" "
  return res

def calculation():
    n = int(a.get())
    e.set(loadedWithValueReturns(n))
def delete_all():
    a.set("")
    e.set("")

root = Tk()
root.title("Lab13")
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