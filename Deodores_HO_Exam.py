import tkinter as tk
from tkinter import messagebox

stored_username = ""
stored_password = ""

window = tk.Tk()
window.title("Module 10 Exam")
window.geometry("300x200")

tk.Label(window, text="Welcome!", font=("Arial", 14)).pack(pady=10)

def open_register():
    reg = tk.Toplevel(window)
    reg.title("Register")
    reg.geometry("300x200")
    reg.configure(bg="green")

    username = tk.StringVar()
    password = tk.StringVar()
    show_pass = tk.BooleanVar()

    def toggle_password():
        if show_pass.get():
            pass_entry.config(show="")
        else:
            pass_entry.config(show="*")

    def register_user():
        global stored_username, stored_password

        user = username.get()
        pwd = password.get()

        if len(pwd) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters")
        else:
            stored_username = user
            stored_password = pwd
            messagebox.showinfo("Success", "You have successfully registered!")

    tk.Label(reg, text="Register", bg="green", font=("Arial", 14)).pack(pady=5)

    tk.Label(reg, text="Username:", bg="green").pack()
    tk.Entry(reg, textvariable=username).pack()

    tk.Label(reg, text="Password:", bg="green").pack()
    pass_entry = tk.Entry(reg, textvariable=password, show="*")
    pass_entry.pack()

    tk.Checkbutton(reg, text="See Password",
                   variable=show_pass,
                   command=toggle_password,
                   bg="green").pack()

    tk.Button(reg, text="Register", command=register_user).pack(pady=5)

def open_login():
    log = tk.Toplevel(window)
    log.title("Log In")
    log.geometry("300x200")
    log.configure(bg="red")

    username = tk.StringVar()
    password = tk.StringVar()
    show_pass = tk.BooleanVar()

    def toggle_password():
        if show_pass.get():
            pass_entry.config(show="")
        else:
            pass_entry.config(show="*")

    def login_user():
        if username.get() == stored_username and password.get() == stored_password:
            messagebox.showinfo("Success", "Login Successful!")
        else:
            messagebox.showerror("Error", "Incorrect Username or Password")

    tk.Label(log, text="Log In", bg="red", font=("Arial", 14)).pack(pady=5)

    tk.Label(log, text="Username:", bg="red").pack()
    tk.Entry(log, textvariable=username).pack()

    tk.Label(log, text="Password:", bg="red").pack()
    pass_entry = tk.Entry(log, textvariable=password, show="*")
    pass_entry.pack()

    tk.Checkbutton(log, text="See Password",
                   variable=show_pass,
                   command=toggle_password,
                   bg="red").pack()

    tk.Button(log, text="Log In", command=login_user).pack(pady=5)

tk.Button(window, text="Register", bg="blue", fg="white",
          width=20, command=open_register).pack(pady=5)

tk.Button(window, text="Log In", bg="green", fg="white",
          width=20, command=open_login).pack(pady=5)

window.mainloop()
