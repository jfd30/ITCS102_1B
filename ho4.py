import tkinter as tk
from tkinter import Toplevel
from datetime import datetime

# Main window
root = tk.Tk()
root.title("Profile Builder")
root.geometry("400x450")

# Variables
name_var = tk.StringVar()
gender_var = tk.StringVar()

day_var = tk.StringVar()
month_var = tk.StringVar()
year_var = tk.StringVar()

hobby_read = tk.IntVar()
hobby_sports = tk.IntVar()
hobby_music = tk.IntVar()

# --- UI ---

# Name
tk.Label(root, text="Enter Name:").pack()
tk.Entry(root, textvariable=name_var).pack()

# Birthday input
tk.Label(root, text="Enter Birthday (DD MM YYYY):").pack()
tk.Entry(root, textvariable=day_var, width=5).pack()
tk.Entry(root, textvariable=month_var, width=5).pack()
tk.Entry(root, textvariable=year_var, width=8).pack()

# Gender
tk.Label(root, text="Select Gender:").pack()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").pack()

# Hobbies
tk.Label(root, text="Select Hobbies:").pack()
tk.Checkbutton(root, text="Reading", variable=hobby_read).pack()
tk.Checkbutton(root, text="Sports", variable=hobby_sports).pack()
tk.Checkbutton(root, text="Music", variable=hobby_music).pack()

# --- Function ---
def calculate_age(day, month, year):
    today = datetime.today()
    birthdate = datetime(year, month, day)

    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

def show_output():
    try:
        name = name_var.get()
        gender = gender_var.get()

        day = int(day_var.get())
        month = int(month_var.get())
        year = int(year_var.get())

        age = calculate_age(day, month, year)

        hobbies = []
        if hobby_read.get():
            hobbies.append("Reading")
        if hobby_sports.get():
            hobbies.append("Sports")
        if hobby_music.get():
            hobbies.append("Music")

        hobbies_text = ", ".join(hobbies) if hobbies else "None"

        # Create TopLevel window
        top = Toplevel(root)
        top.title("Profile Output")
        top.geometry("300x250")

        result = f"Name: {name}\nGender: {gender}\nAge: {age}\nHobbies: {hobbies_text}"

        tk.Label(top, text="Profile Summary", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Label(top, text=result).pack(pady=10)

    except:
        tk.Label(root, text="Invalid date input!", fg="red").pack()

# Button
tk.Button(root, text="Generate Profile", command=show_output).pack(pady=20)

# Run
root.mainloop()
