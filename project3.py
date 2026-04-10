import tkinter as tk
from tkinter import messagebox
def convert_inches_to_cm():
    try:
        inches = float(entry_inches.get())
        centimeters = inches * 2.54
        label_result.config(text=f"Length in Centimeters: {centimeters:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric value for inches.")
root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("350x200")
label_instruction = tk.Label(root, text="Enter length in inches:", font=("Arial", 10))
label_instruction.pack(pady=10)
entry_inches = tk.Entry(root, font=("Arial", 10))
entry_inches.pack(pady=5)
button_convert = tk.Button(root, text="Convert", command=convert_inches_to_cm, 
                           bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
button_convert.pack(pady=15)
label_result = tk.Label(root, text="Length in Centimeters: ", font=("Arial", 11, "bold"))
label_result.pack(pady=5)
root.mainloop()
