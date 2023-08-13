import tkinter as tk
root = tk.Tk()
def change_font():
    lab.config(font = (e.get(), 11))
lab = tk.Label(root, text = 'text label')
lab.pack()
tk.Button(root, text = 'сменить шрифт', command = change_font).pack()
e = tk.Entry(root)
e.pack()
root.mainloop()