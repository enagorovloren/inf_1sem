from tkinter import *
from tkinter import ttk

def solve():
    label["text"] = eval(en.get())

root = Tk()

root.geometry("400x400")
root.title('Калькулятор')

text = ttk.Label(text="Пожалуйста, не пишите сюда консольные команды!")
text.pack()

en = Entry()
en.pack()

btn = ttk.Button(text="Вычислить",command=solve)
btn.pack()

label = ttk.Label()
label.pack()

root.mainloop()
