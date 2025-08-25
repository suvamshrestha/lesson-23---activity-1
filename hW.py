import tkinter as tk
from tkinter import messagebox
def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        messagebox.showinfo("Result", f"The product is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
root = tk.Tk()
root.title("Multiply Two Numbers")
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)
tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)
tk.Button(root, text="Multiply", command=multiply).pack(pady=10)
root.mainloop()
