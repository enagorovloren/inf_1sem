from tkinter import *
from tkinter import ttk

def solve():
    val = (float(en1.get())) / ((float(en2.get()))/100)**2
    label["text"] = val
    if val <= 16:
        l3["text"] = "Выраженный дефицит массы тела"
    elif val <=18.5:
        l3["text"] = "Дефицит массы тела"
    elif val <=25:
        l3["text"] = "Норма"
    elif val <=30:
        l3["text"] = "Предожирение"
    elif val <=35:
        l3["text"] = "Ожирение 1 степени"
    elif val <=40:
        l3["text"] = "Ожирение 2 степени"
    else:
        l3["text"] = "Ожирение 3 степени"
    

root = Tk()

root.title("ИМТ")
root.geometry("400x400")

l1 = ttk.Label(text="Введите Ваш вес: ")
l1.pack()
en1 = ttk.Entry()
en1.pack()

l2 = ttk.Label(text="Введите ваш рост(см): ")
l2.pack()
en2 = ttk.Entry()
en2.pack()

btn = ttk.Button(text="Вычислить", command=solve)
btn.pack()

label = ttk.Label()
label.pack()
l3 = ttk.Label()
l3.pack()

root.mainloop()
