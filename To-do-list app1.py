import customtkinter as ct
from tkinter import messagebox
from PIL import Image, ImageTk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("600x600")
        self.root.resizable(False,False)

        # Create frames
        self.menu_frame = ct.CTkFrame(self.root, corner_radius=0)
        self.menu_frame.pack(fill="x")

        self.task_frame = ct.CTkFrame(self.root)
        self.task_frame.pack(fill="both", expand=True)

        # Create logo widget
        try:
            self.logo_img = Image.open("C:\\Users\\ayush\\OneDrive\\Desktop\\New folder\\OIP.png")
            self.logo_img = ImageTk.PhotoImage(self.logo_img.resize((20, 20)))
        except Exception as e:
            print("Error loading logo image:", str(e))
            self.logo_img = None

        # self.logo_widget = ct.CTkLabel(self.menu_frame, image=self.logo_img)
        # self.logo_widget.image = self.logo_img  # Keep a reference to the image
        # self.logo_widget.pack(side="left", padx=20, pady=20)

        # Create input field and add button
        self.input_field = ct.CTkEntry(self.menu_frame, width=430)
        self.input_field.pack(side="left", padx=10, pady=10)

        self.add_button = ct.CTkButton(self.menu_frame, text="ADD TASK", command=self.add_task,fg_color="teal",hover_color="black")
        self.add_button.pack(side="left", padx=10, pady=10)

        # Create list box
        self.task_list_frame = ct.CTkFrame(self.task_frame)
        self.task_list_frame.pack(fill="both", expand=True)

        self.task_list = []
                

        # Create delete button
        self.delete_button = ct.CTkButton(self.task_frame, text="Delete Task", command=self.delete_task,fg_color="teal",hover_color="red")
        self.delete_button.pack(fill="x", padx=10, pady=10)

        # Create complete button
        self.complete_button = ct.CTkButton(self.task_frame, text="Complete Task", command=self.complete_task, fg_color="teal",hover_color="green")
        self.complete_button.pack(fill="x", padx=10, pady=10)

        # Load existing tasks
        self.load_tasks()

    def add_task(self):
        task = self.input_field.get()
        if task:  # Check for empty tasks
            self.task_list.append({"text": task,"complete": False, "var": ct.IntVar(), "checkbox": None})
            self.input_field.delete(0, 'end')
            self.update_task_list()

    def delete_task(self):
        for i, task in enumerate(self.task_list):
            if task["var"].get():
                del self.task_list[i]
        self.update_task_list()

    def complete_task(self):
        for task in self.task_list:
            if task["var"].get():
                task["complete"] = True
        self.update_task_list()

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                tasks = [line.strip().split(';') for line in f.readlines()]
                for task in tasks:
                    self.task_list.append({"text": task[0], "var": ct.IntVar(), "complete": task[1] == 'True'})
            self.update_task_list()
        except FileNotFoundError:
            pass  # No tasks file found, do nothing
        

    def update_task_list(self):
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()
            
        for i, task in enumerate(self.task_list):
            task_frame = ct.CTkFrame(self.task_list_frame)
            task_frame.pack(fill="x")
        
        # for task in self.task_list:
        #     task_frame = ct.CTkFrame(self.task_list_frame) 
        #     task_frame.pack(fill="x")
            
            var = task["var"]
            checkbox = ct.CTkCheckBox(task_frame, variable=task["var"], text="",width=20,fg_color="green")
            checkbox.pack(side="left", padx=(0,5))

            task_text = task["text"]
            if task["complete"]:
                task_text =  f'\u0336'.join(c for c in task_text)  # Strike through text
                task_label = ct.CTkLabel(task_frame, text=task_text, font=("Helvetica", 20), wraplength=550, text_color="green")
            else:
                task_label = ct.CTkLabel(task_frame, text=task_text, font=("Helvetica", 20), wraplength=550)
            task_label.pack( side="left",fill="x", expand=True)  # Fill and expand to fill available space
            
            # task_label = ct.CTkLabel(task_frame, text=task_text, font=("Helvetica", 20), wraplength=550)
            # task_label.pack( side="left",fill="x", expand=True)  # Fill and expand to fill available space

            # Add a separator between tasks
            separator = ct.CTkFrame(self.task_list_frame, height=2, corner_radius=0, fg_color="gray")
            separator.pack(fill="x", pady=(5, 5))

if __name__ == "__main__":
    root = ct.CTk()
    app = ToDoListApp(root)
    root.mainloop()