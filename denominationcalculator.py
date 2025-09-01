from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
def open_calculator():
    welcome_win.destroy()
    root = Tk()
    root.title("Denomination Calculator")
    root.geometry("400x400")
    root.configure(bg="#f0f0f0")
    def calculate():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            amount %= 100
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer amount.")
    def reset():
        entry.delete(0, END)
        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)
    def exit_app():
        root.destroy()
    Label(root, text=" total amount", bg='light grey', font=('Arial', 11)).place(x=120, y=30)
    entry = Entry(root)
    entry.place(x=120, y=60)
    Label(root, text="No. of 2000 notes", bg='light grey', font=('Arial', 11)).place(x=120, y=100)
    Label(root, text="No. of 500 notes", bg='light grey', font=('Arial', 11)).place(x=120, y=140)
    Label(root, text="No. of 100 notes", bg='light grey', font=('Arial', 11)).place(x=120, y=180)
    t1 = Entry(root)
    t1.place(x=120, y=120)
    t2 = Entry(root)
    t2.place(x=120, y=160)
    t3 = Entry(root)
    t3.place(x=120, y=200)
    Button(root, text="Calculate", command=calculate, bg='light grey', font=('Arial', 11)).place(x=50, y=250)
    Button(root, text="Reset", command=reset, bg='light grey', font=('Arial', 11)).place(x=150, y=250)
    Button(root, text="Exit", command=exit_app, bg='light grey', font=('Arial', 11)).place(x=250, y=250)
    root.mainloop()
welcome_win = Tk()
welcome_win.title("Welcome")
welcome_win.geometry("400x400")
welcome_win.configure(bg="#f0f0f0")
try:
    img = Image.open("143.jpg")
    img = img.resize((300,200))
    welcome_photo = ImageTk.PhotoImage(img)
    Label(welcome_win, image=welcome_photo, bg = 'white').pack(pady=30)
except:
    Label(welcome_win, text="welcome tp denomination calculator", font = ('Arial', 14), bg="white", fg="black").pack(pady=80)
Button(welcome_win, text="lets get started", command=open_calculator, font=('Arial', 12), bg="green", fg="white").pack(pady=20)
welcome_win.mainloop()