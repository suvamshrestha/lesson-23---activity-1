import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar
import os
from datetime import datetime

class RestaurantOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Order Management")
        self.root.geometry("950x650")

        # === Background Image ===
        bg_image = Image.open("as.jpg").resize((950, 650))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # === Logo ===
        fg_image = Image.open("ty.jpeg").resize((100, 100))
        self.fg_photo = ImageTk.PhotoImage(fg_image)
        fg_label = tk.Label(root, image=self.fg_photo, bg="#ffffff")
        fg_label.place(x=30, y=20)

        # === Calendar ===
        self.cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
        self.cal.place(x=720, y=20)

        # === Customer Name & Table ===
        tk.Label(root, text="Customer Name:", font=('Arial', 12), bg="#f0f0f0").place(x=50, y=140)
        self.name_entry = tk.Entry(root, font=('Arial', 12), width=20)
        self.name_entry.place(x=200, y=140)

        tk.Label(root, text="Table Number:", font=('Arial', 12), bg="#f0f0f0").place(x=50, y=180)
        self.table_entry = tk.Entry(root, font=('Arial', 12), width=20)
        self.table_entry.place(x=200, y=180)

        # === Menu Items with Quantity ===
        tk.Label(root, text="Select Items & Quantity:", font=('Arial', 12, 'bold'), bg="#f0f0f0").place(x=50, y=220)
        self.items = {
            "Pizza": {"price": 250, "var": tk.IntVar(), "qty": tk.StringVar(value="1")},
            "Pasta": {"price": 180, "var": tk.IntVar(), "qty": tk.StringVar(value="1")},
            "Salad": {"price": 120, "var": tk.IntVar(), "qty": tk.StringVar(value="1")},
            "Soup": {"price": 100, "var": tk.IntVar(), "qty": tk.StringVar(value="1")},
            "Juice": {"price": 90, "var": tk.IntVar(), "qty": tk.StringVar(value="1")}
        }

        y = 250
        for item, data in self.items.items():
            tk.Checkbutton(root, text=f"{item} - ₹{data['price']}",
                           variable=data["var"], bg="#f0f0f0", font=('Arial', 11)).place(x=70, y=y)
            tk.Entry(root, textvariable=data["qty"], width=5).place(x=250, y=y+2)
            y += 30

        # === Buttons ===
        tk.Button(root, text="Submit Order", command=self.submit_order,
                  font=('Arial', 12, 'bold'), bg="green", fg="white").place(x=70, y=430)

        tk.Button(root, text="Save & Print Bill", command=self.save_and_print,
                  font=('Arial', 12, 'bold'), bg="blue", fg="white").place(x=220, y=430)

        # === Bill Display ===
        self.output_text = tk.Text(root, height=15, width=50, font=('Courier', 11))
        self.output_text.place(x=400, y=270)

    def submit_order(self):
        self.output_text.delete("1.0", tk.END)
        customer = self.name_entry.get().strip()
        table_no = self.table_entry.get().strip()
        order_date = self.cal.get_date()
        total = 0
        items_ordered = []

        if not customer or not table_no:
            messagebox.showwarning("Missing Info", "Please enter customer name and table number.")
            return

        for item, data in self.items.items():
            if data["var"].get():
                try:
                    qty = int(data["qty"].get())
                    if qty < 1:
                        raise ValueError
                except ValueError:
                    messagebox.showerror("Invalid Input", f"Enter valid quantity for {item}.")
                    return

                price = data["price"] * qty
                items_ordered.append((item, qty, data["price"], price))
                total += price

        if not items_ordered:
            messagebox.showwarning("No Items", "Please select at least one item.")
            return

        # Bill Text
        bill_text = f"RESTAURANT BILL\nDate: {order_date}\nCustomer: {customer}\nTable No: {table_no}\n"
        bill_text += "-" * 46 + "\n"
        bill_text += f"{'Item':<12}{'Qty':<6}{'Rate':<8}{'Total'}\n"
        bill_text += "-" * 46 + "\n"
        for item, qty, rate, price in items_ordered:
            bill_text += f"{item:<12}{qty:<6}{rate:<8}₹{price}\n"
        bill_text += "-" * 46 + f"\nTOTAL AMOUNT: ₹{total}\n"
        bill_text += "Thank you for dining with us!"

        self.bill_text = bill_text
        self.output_text.insert(tk.END, bill_text)
        messagebox.showinfo("Order Submitted", "Order recorded and bill generated!")

    def save_and_print(self):
        if not hasattr(self, 'bill_text'):
            messagebox.showwarning("No Bill", "Please submit order before saving.")
            return

        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"bill_{now}.txt"
        with open(filename, "w") as file:
            file.write(self.bill_text)

        messagebox.showinfo("Saved", f"Bill saved as {filename}")
        os.startfile(filename, "print")


# === Launch the App ===
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderApp(root)
    root.mainloop()