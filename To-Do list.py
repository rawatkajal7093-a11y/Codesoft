from tkinter import *

def add_task():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)

def update_task():
    try:
        index = listbox.curselection()[0]
        task = entry.get()
        listbox.delete(index)
        listbox.insert(index, task)
        entry.delete(0, END)
    except:
        pass

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        pass

def complete_task():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        if not task.startswith("✔ "):
            listbox.delete(index)
            listbox.insert(index, "✔ " + task)
    except:
        pass