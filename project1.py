import tkinter as tk
from tkinter import messagebox
def calculate():
    try:
        product = float(e1.get()) * float(e2.get())
        lbl_res.config(text=f"Result: {product}")
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")
root = tk.Tk()
root.title("Calculator")
e1, e2 = tk.Entry(root), tk.Entry(root)
e1.pack(); e2.pack()
tk.Button(root, text="Multiply", command=calculate).pack()
lbl_res = tk.Label(root, text="Result: ")
lbl_res.pack()
root.mainloop()
