import tkinter as tk
def convert_length():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{inches} inches = {cm:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number")
root = tk.Tk()
root.title("Length Converter App")
tk.Label(root, text="Enter length in inches:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)
convert_btn = tk.Button(root, text="Convert", command=convert_length)
convert_btn.pack(pady=5)
result_label = tk.Label(root, text="")
result_label.pack(pady=5)
root.mainloop()
