from tkinter import *
root = Tk()
root.geometry("700x700")
root.title("Main Window")
def topwin():
    top = Toplevel()
    top.geometry("400x400")
    top.title("Top Level Window")
    L2 = Label(top,text="this is a top level window")
    L2.pack()
    top.mainloop()
L = Label(root,text="this is a root window")
BTN = Button(root,text="click here to open a top level window",command=topwin)
L.pack()
BTN.pack()
root.mainloop()
    
