import tkinter as tk
from datetime import datetime

window = tk.Tk()
window.title("Profile Builder")
window.geometry("650x300")
window.configure(bg="#7ED957") 


fname = tk.StringVar()
mname = tk.StringVar()
lname = tk.StringVar()
byear = tk.StringVar()
age_text = tk.StringVar(value="Computing Age...")
gender = tk.StringVar()


def compute_age(event):
    try:
        year = int(byear.get())
        current = datetime.now().year
        age = current - year
        age_text.set(f"Age: {age}")
    except:
        age_text.set("Invalid Year")

def change_color():
    if gender.get() == "Male":
        color = "#AEE2FF"
    else:
        color = "#FFB6C1"

    window.config(bg=color)
    form_frame.config(bg=color)

    for widget in form_frame.winfo_children():
        if isinstance(widget, (tk.Label, tk.Radiobutton)):
            widget.config(bg=color)

def hover_in(e):
    submit_btn.config(bg="lightgreen")

def hover_out(e):
    submit_btn.config(bg="SystemButtonFace")

def show_id():
    top = tk.Toplevel(window)
    top.title("Student ID")
    top.geometry("300x200")

    full = f"{fname.get()} {mname.get()} {lname.get()}"

    tk.Label(top, text="STUDENT ID", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(top, text=f"Name: {full}").pack()
    tk.Label(top, text=age_text.get()).pack()
    tk.Label(top, text=f"Gender: {gender.get()}").pack()

tk.Label(window, text="Profile Builder", font=("Arial", 16, "bold"),
         bg="#7ED957").pack(pady=5)

form_frame = tk.Frame(window, bg="#7ED957", bd=2, relief="groove")
form_frame.pack(padx=20, pady=10, fill="both")

tk.Entry(form_frame, textvariable=fname, width=22).grid(row=0, column=0, padx=10, pady=5)
tk.Entry(form_frame, textvariable=mname, width=22).grid(row=0, column=1, padx=10, pady=5)
tk.Entry(form_frame, textvariable=lname, width=22).grid(row=0, column=2, padx=10, pady=5)

tk.Label(form_frame, text="First Name", bg="#7ED957").grid(row=1, column=0)
tk.Label(form_frame, text="Middle Name", bg="#7ED957").grid(row=1, column=1)
tk.Label(form_frame, text="Last Name", bg="#7ED957").grid(row=1, column=2)

birth_entry = tk.Entry(form_frame, textvariable=byear, width=22)
birth_entry.grid(row=2, column=0, padx=10, pady=5)
birth_entry.bind("<Return>", compute_age)

tk.Label(form_frame, text="Birth Year", bg="#7ED957").grid(row=3, column=0)

tk.Label(form_frame, textvariable=age_text,
         font=("Arial", 16, "italic"),
         bg="#7ED957").grid(row=2, column=1, columnspan=2, pady=10)

tk.Label(form_frame, text="Gender", bg="#7ED957").grid(row=4, column=0)

tk.Radiobutton(form_frame, text="Male", variable=gender,
               value="Male", command=change_color,
               bg="#7ED957").grid(row=4, column=1, sticky="w")

tk.Radiobutton(form_frame, text="Female", variable=gender,
               value="Female", command=change_color,
               bg="#7ED957").grid(row=4, column=2, sticky="w")

submit_btn = tk.Button(window, text="Submit",
                       font=("Arial", 12, "bold"),
                       command=show_id)
submit_btn.pack(pady=10)

submit_btn.bind("<Enter>", hover_in)
submit_btn.bind("<Leave>", hover_out)

window.mainloop()
