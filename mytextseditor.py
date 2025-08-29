from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import simpledialog, messagebox
import tkinter.font as tkFont
window = Tk()
window.title("My Text Editor")
window.geometry("800x600")
dark_mode = False
font_styles = {
"Regular": {"weight": "normal", "slant": "roman"},
"Bold": {"weight": "bold", "slant": "roman"},
"Italic": {"weight": "normal", "slant": "italic"},
"Bold-Italic": {"weight": "bold", "slant": "italic"}
}
text_font = tkFont.Font(family="Arial", size=12, weight="normal", slant="italic")
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)
top_frame = Frame(window)
top_frame.grid(row=0, column=0, sticky="ew")
Label(top_frame, text="Font Style").pack(side=LEFT, padx=5)
Style_var = StringVar(value="Italic")
def change_font_style():
    style = Style_var.get()
    text_font.config(**font_styles[style])
style_menu = OptionMenu(top_frame, Style_var, *font_styles.keys(),command=change_font_style)
style_menu.pack(side=LEFT)
text_area=Text(window, font=text_font, wrap=WORD)
text_area.grid(row=1, column=0, sticky="nsew")
scroll = Scrollbar(window, command=text_area.yview)
scroll.grid(row=1, column=1, sticky="ns")
text_area.config(yscrollcommand=scroll.set)
# ---------- Functions ----------
def open_file(event=None):
    file_path = askopenfilename()
    if file_path:
       with open(file_path, "r") as file:
           content = file.read()
           text_area.delete(1.0, END)
           text_area.insert(END, content)
def save_file(event=None):
    file_path = asksaveasfilename(defaultextension=".txt")
    if file_path:
       with open(file_path, "w") as file:
           file.write(text_area.get(1.0, END))
def show_word_count(event=None):
    text = text_area.get(1.0, END)
    words = text.split()
    characters = len(text.strip())
    messagebox.showinfo("Word Count", f"Words: {len(words)}\nCharacters: {characters}")
def change_font_size():
    size = simpledialog.askinteger("Font Size", "Enter font size:", minvalue=8, maxvalue=72)
    if size:
        text_font.config(size=size)
def find_replace(event=None):
    find = simpledialog.askstring("Find", "Enter text to find:")
    replace = simpledialog.askstring("Replace", "Replace with:")
    if find is not None and replace is not None:
       content = text_area.get(1.0, END)
       new_content = content.replace(find, replace)
       text_area.delete(1.0, END)
       text_area.insert(END, new_content)
def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
       text_area.config(bg="black", fg="white", insertbackground="white")
    else:
       text_area.config(bg="white", fg="black", insertbackground="black")
# ---------- Menus ----------
menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open (Ctrl+O)", command=open_file)
file_menu.add_command(label="Save (Ctrl+S)", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Find & Replace (Ctrl+F)", command=find_replace)
edit_menu.add_command(label="Word Count (Ctrl+W)", command=show_word_count)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
view_menu = Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Change Font Size", command=change_font_size)
view_menu.add_command(label="Toggle Dark Mode", command=toggle_dark_mode)
menu_bar.add_cascade(label="View", menu=view_menu)
window.config(menu=menu_bar)
# ---------- Keyboard Shortcuts ----------
window.bind("<Control-o>", open_file)
window.bind("<Control-s>", save_file)
window.bind("<Control-f>", find_replace)
window.bind("<Control-w>", show_word_count)
# ---------- Start App ----------
window.mainloop()

