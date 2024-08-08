import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []
        self.setup_gui()
        
    def setup_gui(self):
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50, height=15)
        self.task_listbox.pack(pady=20)
        
        tk.Button(self.root, text="Add Task", command=self.add_task).pack(pady=5)
        tk.Button(self.root, text="Update Task", command=self.update_task).pack(pady=5)
        tk.Button(self.root, text="Delete Task", command=self.delete_task).pack(pady=5)
        
        self.load_tasks()
        self.update_task_listbox()
        
    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task description:")
        if task:
            self.tasks.append({"description": task, "completed": False})
            self.save_tasks()
            self.update_task_listbox()
        
    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.tasks[task_index]["completed"] = not self.tasks[task_index]["completed"]
            self.save_tasks()
            self.update_task_listbox()
        else:
            messagebox.showwarning("Update Task", "No task selected.")
    
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            del self.tasks[task_index]
            self.save_tasks()
            self.update_task_listbox()
        else:
            messagebox.showwarning("Delete Task", "No task selected.")
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task["completed"] else "Pending"
            self.task_listbox.insert(tk.END, f"{task['description']} [{status}]")
    
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.tasks = []

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
