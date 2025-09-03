import tkinter as tk
from tkinter import messagebox
def check_strength():
    password = entry.get()
    strength = ""
    if len(password) == 0:
        strength = "Please enter a password!"
    elif len(password) < 4:
        strength = "Weak"
    elif len(password) < 8:
        strength = "Moderate"
    else:
        strength = "Strong"
    messagebox.showinfo("Password Strength", f"Your password is: {strength}")
root = tk.Tk()
root.title("Password Strength Checker")
label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)
btn = tk.Button(root, text="Check Strength", command=check_strength)
btn.pack(pady=10)
root.mainloop()
