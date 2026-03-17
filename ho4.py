import tkinter as tk
from tkinter import Toplevel
import time

# Main window
root = tk.Tk()
root.title("Profile Builder")
root.geometry("400x450")

# Variables
name_var = tk.StringVar()
gender_var = tk.StringVar()

birth_day = tk.IntVar()
birth_month = tk.IntVar()
birth_year = tk.IntVar()

hobby_read = tk.IntVar()
hobby_sports = tk.IntVar()
hobby_music = tk.IntVar()

# --- UI Elements ---

# Name
tk.Label(root, text="Enter Name:").pack()
tk.Entry(root, textvariable=name_var).pack()

# Birthday
tk.Label(root, text="Enter Birthday (DD MM YYYY):").pack()
tk.Entry(root, textvariable=birth_day, width=5).pack()
tk.Entry(root, textvariable=birth_month, width=5).pack()
tk.Entry(root, textvariable=birth_year, width=8).pack()

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

# Output label
output_label = tk.Label(root, text="", fg="blue")
output_label.pack(pady=10)

# --- Function to calculate age ---
def calculate_age(day, month, year):
    try:
        birth_time = time.strptime(f"{day} {month} {year}", "%d %m %Y")
        birth_seconds = time.mktime(birth_time)
        current_seconds = time.time()

        age_years = int((current_seconds - birth_seconds) / (365.25 * 24 * 60 * 60))
        return age_years
    except:
        return "Invalid Date"

# --- Show Profile (Second Window) ---
def show_profile():
    top = Toplevel(root)
    top.title("Profile Preview")
    top.geometry("300x300")

    name = name_var.get()
    gender = gender_var.get()

    day = birth_day.get()
    month = birth_month.get()
    year = birth_year.get()

    age = calculate_age(day, month, year)

    hobbies = []
    if hobby_read.get():
        hobbies.append("Reading")
    if hobby_sports.get():
        hobbies.append("Sports")
    if hobby_music.get():
        hobbies.append("Music")

    hobbies_text = ", ".join(hobbies) if hobbies else "None"

    profile_text = f"""Name: {name}
Gender: {gender}
Age: {age}
Hobbies: {hobbies_text}"""

    tk.Label(top, text="Preview", font=("Arial", 12, "bold")).pack(pady=5)
    tk.Label(top, text=profile_text).pack(pady=10)

    def confirm():
        output_label.config(text=profile_text)
        top.destroy()

    tk.Button(top, text="Confirm", command=confirm).pack(pady=10)

# Button
tk.Button(root, text="Build Profile", command=show_profile).pack(pady=15)

# Run
root.mainloop()
