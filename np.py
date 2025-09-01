import tkinter as tk
from tkinter import messagebox
def calculate_interest():
    try:
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())
        si = (principal * time * rate) / 100
        ci = principal * ((1 + rate/100) ** time) - principal
        messagebox.showinfo("Interest Result",
                            f"Simple Interest = {si:.2f}\nCompound Interest = {ci:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
root = tk.Tk()
root.title("Interest Calculator")
tk.Label(root, text="Principal Amount:").grid(row=0, column=0, padx=10, pady=5)
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Time (in years):").grid(row=1, column=0, padx=10, pady=5)
entry_time = tk.Entry(root)
entry_time.grid(row=1, column=1, padx=10, pady=5)
tk.Label(root, text="Rate of Interest (%):").grid(row=2, column=0, padx=10, pady=5)
entry_rate = tk.Entry(root)
entry_rate.grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Calculate", command=calculate_interest).grid(row=3, columnspan=2, pady=10)
root.mainloop()
