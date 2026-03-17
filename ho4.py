     import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Main window
root = tk.Tk()
root.title("Student ID Generator")
root.geometry("400x400")

# Variables
first_name = tk.StringVar()
middle_name = tk.StringVar()
last_name = tk.StringVar()
birth_year = tk.StringVar()
age = tk.StringVar()
gender = tk.StringVar()

# Functions
def calculate_age(event):
    try:
        year = int(birth_year.get())
        current_year = datetime.now().year
        computed_age = current_year - year
        age.set(str(computed_age))
    except:
        age.set("Invalid")

def change_bg():
    if gender.get() == "Male":
        root.config(bg="lightblue")
    elif gender.get() == "Female":
        root.config(bg="lightpink")

def on_enter(e):
    submit_btn.config(bg="lightgreen")

def on_leave(e):
    submit_btn.config(bg="SystemButtonFace")

def generate_id():
    top = tk.Toplevel(root)
    top.title("Student ID Card")
    top.geometry("300x200")

    full_name = f"{first_name.get()} {middle_name.get()} {last_name.get()}"

    tk.Label(top, text="STUDENT ID", font=("Arial", 14, "bold")).pack(pady=5)
    tk.Label(top, text=f"Name: {full_name}").pack()
    tk.Label(top, text=f"Age: {age.get()}").pack()
    tk.Label(top, text=f"Gender: {gender.get()}").pack()

# UI Layout
tk.Label(root, text="First Name").pack()
tk.Entry(root, textvariable=first_name).pack()

tk.Label(root, text="Middle Name").pack()
tk.Entry(root, textvariable=middle_name).pack()

tk.Label(root, text="Last Name").pack()
tk.Entry(root, textvariable=last_name).pack()

tk.Label(root, text="Birth Year").pack()
birth_entry = tk.Entry(root, textvariable=birth_year)
birth_entry.pack()
birth_entry.bind("<Return>", calculate_age)

tk.Label(root, text="Age").pack()
tk.Entry(root, textvariable=age, state="readonly").pack()

tk.Label(root, text="Gender").pack()
tk.Radiobutton(root, text="Male", variable=gender, value="Male", command=change_bg).pack()
tk.Radiobutton(root, text="Female", variable=gender, value="Female", command=change_bg).pack()

submit_btn = tk.Button(root, text="Submit", command=generate_id)
submit_btn.pack(pady=10)

# Hover effect
submit_btn.bind("<Enter>", on_enter)
submit_btn.bind("<Leave>", on_leave)

root.mainloop()   
