from tkinter import *
def show_message():
    name = name_entry.get()
    message = f"Hello, {name}! Welcome to the world of widgets."
    output_text.delete(1.0, END)
    output_text.insert(END, message)
window = Tk()
window.title("Widget Example")
window.geometry("400x300")
label = Label(window, text="Enter your name:", font=("Arial", 14))
label.pack(pady=10)
name_entry = Entry(window, font=("Arial", 14))
name_entry.pack(pady=10)
button = Button(window, text="Submit", command=show_message, font=("Arial", 14))
button.pack(pady=10)
output_text = Text(window, height=5, width=40, font=("Arial", 14))
output_text.pack(pady=10)
window.mainloop()
