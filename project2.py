import tkinter as tk
from datetime import date
from tkinter import messagebox
def calculate_age():
    try:
        birth_day = int(day_entry.get())
        birth_month = int(month_entry.get())
        birth_year = int(year_entry.get())
        today = date.today()
        age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
        result_label.config(text=f"Your current age is: {age} years")
    except ValueError:        
        messagebox.showerror("Input Error", "Please enter valid numeric values for Day, Month, and Year.")
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x250")
tk.Label(root, text="Enter Day (DD):").pack(pady=5)
day_entry = tk.Entry(root)
day_entry.pack()
tk.Label(root, text="Enter Month (MM):").pack(pady=5)
month_entry = tk.Entry(root)
month_entry.pack()
tk.Label(root, text="Enter Year (YYYY):").pack(pady=5)
year_entry = tk.Entry(root)
year_entry.pack()
calculate_btn = tk.Button(root, text="Calculate Age", command=calculate_age, bg="lightblue")
calculate_btn.pack(pady=15)
result_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
result_label.pack()
root.mainloop()
