from tkinter import *
from tkinter import ttk
import pandas as pd
from random import randint

root = Tk()
root.geometry("400x400")
root.title("Films")

films = pd.read_csv('imdb_top_250.csv')

genres = ('Sport', 'Animation', 'Thriller', 'Horror', 'Comedy', 'Fantasy', 'Biography', 'Musical', 'Romance', 'War', 'Family', 'Mystery', 'Action', 'History', 'Crime', 'Adventure', 'Drama', 'Western', 'Music')

genres_dict = {g: [] for g in genres}

for index, row in films.iterrows():
    s = row['Genre'].split(' | ')
    for x in s:
        genres_dict[x].append(row['Title'])

combo = ttk.Combobox(root, values=genres, state="readonly")
combo.pack(pady=20)
combo.current(0)                     # выбрать первый элемент по умолчанию
# combo.set("Drama")                 # либо задать конкретное значение

label = Label(root, text="")
label.pack()


# --- Обработка выбора ---
def on_select(event):
    name = combo.get()
    label['text'] = genres_dict[name][randint(0,len(genres_dict[name])-1)]

combo.bind("<<ComboboxSelected>>", on_select)

root.mainloop()