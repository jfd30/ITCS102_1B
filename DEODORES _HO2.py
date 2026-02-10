import tkinter as tkin

window = tkin.Tk()

window.title("Justin's Profile")
window.geometry("600x600")
window.resizable(True,True)
window.configure(bg="pink")

label = tkin.Label(window,text="Student Profile", font=("arial",32,"bold"),fg="black",bg="pink")
label.pack(side="top",padx=5,pady=10, fill="x")

Name = tkin.Label(window,text="Name: Justin Deodores", font=("arial",16,"bold"),fg="black",bg="pink",anchor="w")
Name.pack(side="top",padx=5,pady=10, fill="x")

Age = tkin.Label(window,text="Age: 19 years old", font=("arial",16,"bold"),fg="black",bg="pink",anchor="w")
Age.pack(side="top",padx=5,pady=10, fill="x")

Course = tkin.Label(window,text="Course: BSIT", font=("arial",16,"bold"),fg="black",bg="pink",anchor="w")
Course.pack(side="top",padx=5,pady=10, fill="x")

Birthday = tkin.Label(window,text="Birthday: November 30, 2006", font=("arial",16,"bold"),fg="black",bg="pink",anchor="w")
Birthday.pack(side="top",padx=5,pady=10, fill="x")

Motto = tkin.Label(window,text="Motto:", font=("arial",16,"bold"),fg="black",bg="pink",anchor="w")
Motto.pack(side="top",padx=5,pady=10, fill="x")

Motto2 = tkin.Label(window,text="Do it or regret it later", font=("arial",16,"bold"),fg="black",bg="pink",anchor="w")
Motto2.pack(side="top",padx=100,pady=10, fill="x")

window.mainloop()
