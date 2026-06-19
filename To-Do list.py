from tkinter import *

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except:
        pass

