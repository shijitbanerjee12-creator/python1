import tkinter as tk
from tkinter import messagebox
def calculate_interest():
    try:
        p = float(entry_principal.get())
        t = float(entry_time.get())
        r = float(entry_rate.get())
        si = (p * r * t) / 100
        ci = p * (pow((1 + r / 100), t)) - p
        label_result.config(text=f"Simple Interest: {si:.2f}\nCompound Interest: {ci:.2f}")    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x300")
tk.Label(root, text="Principal Amount:").pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack()
tk.Label(root, text="Time Period (Years):").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack()
tk.Label(root, text="Rate of Interest (%):").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack()
btn_calculate = tk.Button(root, text="Calculate", command=calculate_interest, bg="lightblue")
btn_calculate.pack(pady=20)
label_result = tk.Label(root, text="", font=("Arial", 10, "bold"))
label_result.pack()
root.mainloop()
