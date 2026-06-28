from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("To-Do List")
root.geometry("500x750")
root.config(bg="#492c7e")

tasks = []

def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        update_list()
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Enter a task")

def update_task():
    try:
        index = listbox.curselection()[0]
        new_task = task_entry.get().strip()

        if new_task == "" or new_task == "Write your task here...":
            messagebox.showwarning("Warning", "Please enter a new task.")
            return

        tasks[index] = new_task
        update_list()

        task_entry.delete(0, END)
        task_entry.insert(0, "Write your task here...")
        task_entry.config(fg="grey")

    except:
        messagebox.showwarning("Warning", "Select a task first.")

def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        update_list()
    except:
        messagebox.showwarning("Warning", "Select a task")

def complete_task():
    try:
        index = listbox.curselection()[0]
        if not tasks[index].startswith("✔ "):
            tasks[index] = "✔ " + tasks[index]
        update_list()
    except:
        messagebox.showwarning("Warning", "Select a task")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        tasks.clear()
        update_list()

def update_list():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

def clear_placeholder(event):
    if task_entry.get() == "Write your task here...":
        task_entry.delete(0, END)
        task_entry.config(fg="black")

def add_placeholder(event):
    if task_entry.get() == "":
        task_entry.insert(0, "Write your task here...")
        task_entry.config(fg="grey")

title = Label(root, text="To-Do List", font=("Segoe UI", 22, "bold"), bg="#f4f4f4")
title.pack(pady=15)

frame = Frame(root, bg="#f4f4f4")
frame.pack(pady= 15)

task_entry = Entry(frame, width=28, font=("Segoe UI", 14), fg="grey")
task_entry.insert(0, "Write your task here...")
task_entry.grid(row=0, column=0, padx=5)       

task_entry.bind("<FocusIn>", clear_placeholder)
task_entry.bind("<FocusOut>", add_placeholder)

Button(frame, text="Add", width=10, bg="#4CAF50", fg="white", command=add_task).grid(row=0, column=1)

listbox = Listbox(root, width=40, height=18, font=("Arial", 14), selectbackground="#6A5ACD")
listbox.pack(pady=20)

button_frame = Frame(root, bg="#6A5ACD")
button_frame.pack(pady=10)

Button(button_frame, text="Update Task", width=20, bg="#3B82F6", fg= "white",
       command=update_task).pack(pady=5)

Button(button_frame, text="Delete Task", width=20, bg="#F44336", fg="white",
       command=delete_task).pack(pady=5)

Button(button_frame, text="Complete Task", width=20, bg="#9C27B0", fg="white",
       command=complete_task).pack(pady=5)

Button(button_frame, text="Clear All Tasks", width=20, bg="#FF9800", fg= "white",
       command=clear_tasks).pack(pady=5)

root.mainloop()