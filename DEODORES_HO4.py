import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Profile Builder")
root.geometry("600x300")
root.configure(bg="#7ED957")  # green background

# Variables
fname = tk.StringVar()
mname = tk.StringVar()
lname = tk.StringVar()
byear = tk.StringVar()
age_text = tk.StringVar(value="Computing Age...")
gender = tk.StringVar()

# Functions
def compute_age(event):
    try:
        year = int(byear.get())
        current = datetime.now().year
        age = current - year
        age_text.set(f"Age: {age}")
    except:
        age_text.set("Invalid Year")

def change_bg():
    if gender.get() == "Male":
        root.configure(bg="#AEE2FF")
    else:
        root.configure(bg="#FFB6C1")

def hover_in(e):
    submit_btn.config(bg="lightgreen")

def hover_out(e):
    submit_btn.config(bg="SystemButtonFace")

def show_id():
    top = tk.Toplevel(root)
    top.title("Student ID")
    top.geometry("300x200")

    full = f"{fname.get()} {mname.get()} {lname.get()}"

    tk.Label(top, text="STUDENT ID", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(top, text=f"Name: {full}").pack()
    tk.Label(top, text=age_text.get()).pack()
    tk.Label(top, text=f"Gender: {gender.get()}").pack()

# Title
tk.Label(root, text="Profile Builder", font=("Arial", 16, "bold"), bg="#7ED957").pack(pady=5)

# Frame (like your box)
frame = tk.Frame(root, bg="#7ED957", bd=2, relief="groove")
frame.pack(padx=20, pady=10, fill="both")

# Row 1 - Names
tk.Entry(frame, textvariable=fname, width=20).grid(row=0, column=0, padx=5, pady=5)
tk.Entry(frame, textvariable=mname, width=20).grid(row=0, column=1, padx=5, pady=5)
tk.Entry(frame, textvariable=lname, width=20).grid(row=0, column=2, padx=5, pady=5)

tk.Label(frame, text="First Name", bg="#7ED957").grid(row=1, column=0)
tk.Label(frame, text="Middle Name", bg="#7ED957").grid(row=1, column=1)
tk.Label(frame, text="Last Name", bg="#7ED957").grid(row=1, column=2)

# Row 2 - Birth Year + Age
tk.Entry(frame, textvariable=byear, width=20).grid(row=2, column=0, padx=5, pady=5)
tk.Label(frame, text="Birth Year", bg="#7ED957").grid(row=3, column=0)

birth_entry = frame.grid_slaves(row=2, column=0)[0]
birth_entry.bind("<Return>", compute_age)

tk.Label(frame, textvariable=age_text, font=("Arial", 14, "italic"), bg="#7ED957").grid(row=2, column=1, columnspan=2)

# Gender
tk.Label(frame, text="Gender", bg="#7ED957").grid(row=4, column=0)

tk.Radiobutton(frame, text="Male", variable=gender, value="Male",
               command=change_bg, bg="#7ED957").grid(row=4, column=1)

tk.Radiobutton(frame, text="Female", variable=gender, value="Female",
               command=change_bg, bg="#7ED957").grid(row=4, column=2)

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=show_id, font=("Arial", 10, "bold"))
submit_btn.pack(pady=10)

submit_btn.bind("<Enter>", hover_in)
submit_btn.bind("<Leave>", hover_out)

root.mainloop()
