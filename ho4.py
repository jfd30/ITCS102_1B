import tkinter as tk
from tkinter import Toplevel

# Main window
root = tk.Tk()
root.title("Profile Builder")
root.geometry("400x400")

# Variables
name_var = tk.StringVar()
gender_var = tk.StringVar()
hobby_read = tk.IntVar()
hobby_sports = tk.IntVar()
hobby_music = tk.IntVar()

# --- UI Elements ---

# Name
tk.Label(root, text="Enter Name:").pack()
tk.Entry(root, textvariable=name_var).pack()

# Gender (Radio Buttons)
tk.Label(root, text="Select Gender:").pack()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").pack()

# Hobbies (Checkbuttons)
tk.Label(root, text="Select Hobbies:").pack()
tk.Checkbutton(root, text="Reading", variable=hobby_read).pack()
tk.Checkbutton(root, text="Sports", variable=hobby_sports).pack()
tk.Checkbutton(root, text="Music", variable=hobby_music).pack()

# Output Label
output_label = tk.Label(root, text="", fg="blue")
output_label.pack(pady=10)

# --- Functions ---

def show_profile():
    # Create second window
    top = Toplevel(root)
    top.title("Profile Preview")
    top.geometry("300x250")

    name = name_var.get()
    gender = gender_var.get()

    hobbies = []
    if hobby_read.get():
        hobbies.append("Reading")
    if hobby_sports.get():
        hobbies.append("Sports")
    if hobby_music.get():
        hobbies.append("Music")

    hobbies_text = ", ".join(hobbies) if hobbies else "None"

    profile_text = f"Name: {name}\nGender: {gender}\nHobbies: {hobbies_text}"

    tk.Label(top, text="Preview", font=("Arial", 12, "bold")).pack(pady=5)
    tk.Label(top, text=profile_text).pack(pady=10)

    # Button to send output back to main window
    def confirm():
        output_label.config(text=profile_text)
        top.destroy()

    tk.Button(top, text="Confirm", command=confirm).pack(pady=10)

# Button to open second window
tk.Button(root, text="Build Profile", command=show_profile).pack(pady=15)

# Run app
root.mainloop()
