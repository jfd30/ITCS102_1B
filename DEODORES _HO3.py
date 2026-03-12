import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")

frame = tk.Frame(window)
frame.grid(row=0, column=0, padx=10, pady=10)

label1 = tk.Label(frame, text="First Number:")
label1.grid(row=0, column=0)

label2 = tk.Label(frame, text="Second Number:")
label2.grid(row=1, column=0)

label_result = tk.Label(frame, text="Result:")
label_result.grid(row=2, column=0)

entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1)

entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1)

result = tk.Label(frame, text="")
result.grid(row=2, column=1)

def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result.config(text=str(num1 + num2))

def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result.config(text=str(num1 - num2))

def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result.config(text=str(num1 * num2))

def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result.config(text=str(num1 / num2))

btn_add = tk.Button(frame, text="Add", command=add)
btn_add.grid(row=3, column=0)

btn_sub = tk.Button(frame, text="Subtract", command=subtract)
btn_sub.grid(row=3, column=1)

btn_mul = tk.Button(frame, text="Multiply", command=multiply)
btn_mul.grid(row=4, column=0)

btn_div = tk.Button(frame, text="Divide", command=divide)
btn_div.grid(row=4, column=1)

window.mainloop()
