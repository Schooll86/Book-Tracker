import tkinter as tk
from tkinter import messagebox
import json, os

file = "books.json"
books = []

def load():
    global books
    if os.path.exists(file):
        books = json.load(open(file, encoding="utf-8"))
        update()

def save():
    json.dump(books, open(file, "w", encoding="utf-8"), ensure_ascii=False, indent=4)

def add():
    title, author, genre, pages = e1.get(), e2.get(), e3.get(), e4.get()
    if not title or not author or not genre or not pages.isdigit():
        return messagebox.showerror("Ошибка", "Проверь ввод")
    books.append({"title":title,"author":author,"genre":genre,"pages":int(pages)})
    update()

def update(data=None):
    lb.delete(0, tk.END)
    for b in (data or books):
        lb.insert(tk.END, f"{b['title']} ({b['genre']}, {b['pages']} стр.)")

def filt():
    g, p = f1.get(), f2.get()
    data=[b for b in books if (g in b['genre'] or not g) and (b['pages']>int(p) if p else True)]
    update(data)

root=tk.Tk()
for t in ["Название","Автор","Жанр","Страницы"]:
    tk.Label(root,text=t).pack()
e1,e2,e3,e4=[tk.Entry(root) for _ in range(4)]
[e.pack() for e in [e1,e2,e3,e4]]

tk.Button(root,text="Добавить",command=add).pack()
lb=tk.Listbox(root,width=50); lb.pack()

tk.Label(root,text="Фильтр жанр").pack()
f1=tk.Entry(root); f1.pack()
tk.Label(root,text="Страницы >").pack()
f2=tk.Entry(root); f2.pack()

tk.Button(root,text="Фильтр",command=filt).pack()
root.protocol("WM_DELETE_WINDOW",lambda:(save(),root.destroy()))
load(); root.mainloop()
