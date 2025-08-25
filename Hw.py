import tkinter as tk
from datetime import date
def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        today = date.today()
        age = today.year - year - ((today.month, today.day) < (month, day))
        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")
root = tk.Tk()
root.title("Age Calculator App")
tk.Label(root, text="Enter your Date of Birth").grid(row=0, column=1, pady=10)
tk.Label(root, text="Day:").grid(row=1, column=0)
tk.Label(root, text="Month:").grid(row=2, column=0)
tk.Label(root, text="Year:").grid(row=3, column=0)
day_entry = tk.Entry(root)
month_entry = tk.Entry(root)
year_entry = tk.Entry(root)
day_entry.grid(row=1, column=1)
month_entry.grid(row=2, column=1)
year_entry.grid(row=3, column=1)
tk.Button(root, text="Calculate Age", command=calculate_age).grid(row=4, column=1, pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=5, column=1, pady=10)
root.mainloop()
