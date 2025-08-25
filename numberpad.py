from tkinter import *
window = Tk()
window.title("Number Pad")
window.geometry("500x500")
entry = Entry(window, width=50, font=("Arial", 25),bd=5, justify="right")
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=20)
def press_num(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))
def clear():
    entry.delete(0, END)
buttons = [('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
               ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
               ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
               ('0', 4, 1)]
for (text, row, col) in buttons:
    Button (window, text=text, width=10, height=3,command=lambda t=text: press_num(t)).grid(row=row, column=col, padx=5, pady=5)
Button (window, text="Clear", width=10, height=3, command=clear).grid(row=4, column=0, padx=5, pady=5)
Button (window, text="Exit", width=10, height=3, command=window.quit).grid(row=4, column=2, padx=5, pady=5)
window.mainloop()


