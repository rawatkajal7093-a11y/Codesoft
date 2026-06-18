# import tkinter as tk
# from tkinter import messagebox
# import json
# from pathlib import Path

# class TodoApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("To-Do List")
#         self.root.geometry("400x500")
        
#         self.data_file = Path("todos.json")
#         self.tasks = self.load_tasks()
        
#         # Input frame
#         input_frame = tk.Frame(root, pady=10)
#         input_frame.pack(fill=tk.X, padx=10)
        
#         self.task_entry = tk.Entry(input_frame, font=("Arial", 12))
#         self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
#         self.task_entry.bind("<Return>", lambda e: self.add_task())
        
#         add_btn = tk.Button(input_frame, text="Add", command=self.add_task)
#         add_btn.pack(side=tk.RIGHT, padx=(5, 0))
        
#         # Task list
#         list_frame = tk.Frame(root)
#         list_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        
#         scrollbar = tk.Scrollbar(list_frame)
#         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
#         self.task_listbox = tk.Listbox(
#             list_frame, 
#             font=("Arial", 11),
#             selectmode=tk.SINGLE,
#             yscrollcommand=scrollbar.set
#         )
#         self.task_listbox.pack(fill=tk.BOTH, expand=True)
#         scrollbar.config(command=self.task_listbox.yview)
        
#         # Buttons frame
#         btn_frame = tk.Frame(root, pady=10)
#         btn_frame.pack(fill=tk.X, padx=10)
        
#         tk.Button(btn_frame, text="Mark Complete", command=self.toggle_complete).pack(side=tk.LEFT)
#         tk.Button(btn_frame, text="Edit", command=self.edit_task).pack(side=tk.LEFT, padx=5)
#         tk.Button(btn_frame, text="Delete", command=self.delete_task).pack(side=tk.LEFT)
#         tk.Button(btn_frame, text="Clear Done", command=self.clear_completed).pack(side=tk.RIGHT)
        
#         self.refresh_list()
    
#     def load_tasks(self) -> list[dict]:
#         if self.data_file.exists():
#             return json.loads(self.data_file.read_text())
#         return []
    
#     def save_tasks(self):
#         self.data_file.write_text(json.dumps(self.tasks, indent=2))
    
#     def refresh_list(self):
#         self.task_listbox.delete(0, tk.END)
#         for task in self.tasks:
#             prefix = "✓ " if task["done"] else "○ "
#             self.task_listbox.insert(tk.END, prefix + task["text"])
#             if task["done"]:
#                 self.task_listbox.itemconfig(tk.END, fg="gray")
    
#     def add_task(self):
#         text = self.task_entry.get().strip()
#         if text:
#             self.tasks.append({"text": text, "done": False})
#             self.save_tasks()
#             self.refresh_list()
#             self.task_entry.delete(0, tk.END)
    
#     def toggle_complete(self):
#         selection = self.task_listbox.curselection()
#         if selection:
#             idx = selection[0]
#             self.tasks[idx]["done"] = not self.tasks[idx]["done"]
#             self.save_tasks()
#             self.refresh_list()
    
#     def edit_task(self):
#         selection = self.task_listbox.curselection()
#         if not selection:
#             return
        
#         idx = selection[0]
#         edit_window = tk.Toplevel(self.root)
#         edit_window.title("Edit Task")
#         edit_window.geometry("300x80")
        
#         entry = tk.Entry(edit_window, font=("Arial", 12))
#         entry.insert(0, self.tasks[idx]["text"])
#         entry.pack(fill=tk.X, padx=10, pady=10)
#         entry.focus()
        
#         def save_edit():
#             new_text = entry.get().strip()
#             if new_text:
#                 self.tasks[idx]["text"] = new_text
#                 self.save_tasks()
#                 self.refresh_list()
#             edit_window.destroy()
        
#         tk.Button(edit_window, text="Save", command=save_edit).pack()
#         entry.bind("<Return>", lambda e: save_edit())
    
#     def delete_task(self):
#         selection = self.task_listbox.curselection()
#         if selection:
#             idx = selection[0]
#             if messagebox.askyesno("Confirm", "Delete this task?"):
#                 del self.tasks[idx]
#                 self.save_tasks()
#                 self.refresh_list()
    
#     def clear_completed(self):
#         self.tasks = [t for t in self.tasks if not t["done"]]
#         self.save_tasks()
#         self.refresh_list()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = TodoApp(root)
#     root.mainloop()
from tkinter import *

# Functions
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

def update_task():
    try:
        selected = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task != "":
            task_listbox.delete(selected)
            task_listbox.insert(selected, new_task)
            task_entry.delete(0, END)
    except:
        pass

def complete_task():
    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)
        task_listbox.delete(selected)
        task_listbox.insert(selected, "✔ " + task)
    except:
        pass

# Main Window
root = Tk()
root.title("To-Do List Application")
root.geometry("400x450")

# Heading
title_label = Label(root, text="To-Do List", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Entry Box
task_entry = Entry(root, width=35, font=("Arial", 12))
task_entry.pack(pady=10)

# Buttons
Button(root, text="Add Task", width=15, command=add_task).pack(pady=5)
Button(root, text="Update Task", width=15, command=update_task).pack(pady=5)
Button(root, text="Complete Task", width=15, command=complete_task).pack(pady=5)
Button(root, text="Delete Task", width=15, command=delete_task).pack(pady=5)

# Listbox to display tasks
task_listbox = Listbox(root, width=40, height=12, font=("Arial", 12))
task_listbox.pack(pady=15)

# Run Application
root.mainloop()