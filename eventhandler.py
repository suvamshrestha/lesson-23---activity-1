from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry('400x300')
def handle_keypress(event):
    print(event.char)
window.bind("<Key>", handle_keypress)
def handle_click(event):
    print("the button was clicked")
button = Button(window, text="Click Me")
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()