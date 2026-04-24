import tkinter as tk
from tkinter import ttk, messagebox
class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")
        self.menu_items = {
            "Burger": 5,
            "Pizza": 8,
            "Pasta": 7,
            "Sandwich": 4,
            "Coffee": 3
        }
        self.exchange_rate = 82
        self.setup_background(root)
        self.frame = ttk.Frame(root, padding=20)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        ttk.Label(self.frame, text="Restaurant Order Management",
                  font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=3, pady=10)
        self.menu_labels = {}
        self.menu_quantities = {}
        row = 1
        for item, price in self.menu_items.items():
            label = ttk.Label(self.frame, text=f"{item} - ${price}")
            label.grid(row=row, column=0, padx=10, pady=5)

            entry = ttk.Entry(self.frame, width=10)
            entry.grid(row=row, column=1, padx=10)

            self.menu_labels[item] = label
            self.menu_quantities[item] = entry

            row += 1
        self.currency_var = tk.StringVar(value="USD")

        ttk.Label(self.frame, text="Currency:").grid(row=row, column=0, pady=10)

        currency_dropdown = ttk.Combobox(
            self.frame,
            textvariable=self.currency_var,
            values=["USD", "INR"],
            state="readonly",
            width=10
        )
        currency_dropdown.grid(row=row, column=1)
        currency_dropdown.current(0)

        self.currency_var.trace_add("write", self.update_menu_prices)
        ttk.Button(self.frame, text="Place Order",
                   command=self.place_order).grid(row=row+1, column=0, columnspan=2, pady=15)
    def setup_background(self, root):
        canvas = tk.Canvas(root, width=800, height=600)
        canvas.pack(fill="both", expand=True)

        try:
            bg_image = tk.PhotoImage(file="background.png")
            bg_image = bg_image.subsample(2, 2)
            canvas.create_image(0, 0, image=bg_image, anchor="nw")
            canvas.image = bg_image
        except:
            canvas.create_text(400, 300, text="Background Image Not Found",
                               font=("Arial", 20))
    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        if currency == "INR":
            symbol = "₹"
            rate = self.exchange_rate
        else:
            symbol = "$"
            rate = 1

        for item, price in self.menu_items.items():
            converted_price = price * rate
            self.menu_labels[item].config(
                text=f"{item} - {symbol}{converted_price:.2f}"
            )

    # 15) Place order
    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"

        currency = self.currency_var.get()

        if currency == "INR":
            symbol = "₹"
            rate = self.exchange_rate
        else:
            symbol = "$"
            rate = 1
        for item, entry in self.menu_quantities.items():
            qty = entry.get()

            if qty.isdigit():
                qty = int(qty)
                if qty > 0:
                    price = self.menu_items[item] * rate
                    cost = price * qty
                    total_cost += cost

                    order_summary += f"{item} x {qty} = {symbol}{cost:.2f}\n"
        if total_cost>0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost:.2f}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least one item.")
if __name__ == "__main__":
    root=tk.Tk()
    root.geometry("800x600")
    app = RestaurantOrderManagement(root)
    root.mainloop()
