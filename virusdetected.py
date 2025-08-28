from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Virus Detected")
root.geometry("400x200")
def msg():
    messagebox.showwarning("warning", "Virus Detected!")
button = Button(root, text="scan for virus", command=msg)
button.place(x=40, y=80)
root.mainloop()
