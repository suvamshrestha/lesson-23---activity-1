import tkinter as TK
from tkinter import messagebox
window = TK.Tk()
window.title("Login Form")
window.geometry('800x800')
TK.Label(window, text="username").pack()
user_entry = TK.Entry(window,justify="left")
user_entry.pack(pady=5)
TK.Label(window, text="password").pack()
pass_entry = TK.Entry(window,show = "*")
pass_entry.pack(pady=5)
def login():
    username = user_entry.get()
    password = pass_entry.get()
    if username == "admin" and password == "admin":
        messagebox.showinfo("Login Status", "Login Successful")
    else:
        messagebox.showerror("Login Status", "Login Failed")
TK.Button(window, text="Login", command=login).pack(pady=20)
TK.mainloop()       

