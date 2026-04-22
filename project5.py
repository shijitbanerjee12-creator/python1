import tkinter as tk
def check_strength():
    password = entry.get()
    length = len(password)
    if length == 0:
        label_result.config(text="Strength: Please enter a password", fg="black")
    elif length < 6:
        label_result.config(text="Strength: Weak", fg="red")
    elif length < 12:
        label_result.config(text="Strength: Medium", fg="orange")
    else:
        label_result.config(text="Strength: Strong", fg="green")
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")
label_instruction = tk.Label(root, text="Enter your password:")
label_instruction.pack(pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)
btn_check = tk.Button(root, text="Check Strength", command=check_strength)
btn_check.pack(pady=15)
label_result = tk.Label(root, text="Strength: ", font=("Arial", 10, "bold"))
label_result.pack(pady=10)
root.mainloop()
