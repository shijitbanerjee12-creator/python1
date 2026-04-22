from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")
label1 = Label(root, text="Welcome to the Denomination Counter!", bg="light blue", font=("Arial", 12))
label1.pack()
def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg="light grey")
    top.geometry("400x400")
    l1 = Label(top, text="Enter total amount:", bg="light grey")
    entry = Entry(top)
    l_head = Label(top, text="Number of notes for each denomination:", bg="light grey", font=("Arial", 10, "bold"))
    l2000 = Label(top, text="2000", bg="light grey")
    l500 = Label(top, text="500", bg="light grey")
    l100 = Label(top, text="100", bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    def calculator():
        try:
            amount = int(entry.get())
            notes2000 = amount // 2000
            amount %= 2000
            
            notes500 = amount // 500
            amount %= 500
            
            notes100 = amount // 100
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            
            t1.insert(END, str(notes2000))
            t2.insert(END, str(notes500))
            t3.insert(END, str(notes100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric amount.")
    btn_calc = Button(top, text="Calculate", command=calculator, bg="black", fg="white")
    l1.place(x=50, y=50)
    entry.place(x=200, y=50)
    btn_calc.place(x=150, y=100)
    
    l_head.place(x=50, y=150)
    l2000.place(x=50, y=200)
    t1.place(x=200, y=200)
    l500.place(x=50, y=250)
    t2.place(x=200, y=250)
    l100.place(x=50, y=300)
    t3.place(x=200, y=300)
    top.mainloop()
def msg():
    res = messagebox.askquestion("Calculate", "Do you want to calculate denominations?")
    if res == 'yes':
        topwin()
button1 = Button(root, text="Let's get started!", command=msg, bg="dark blue", fg="white")
button1.pack(side=BOTTOM, pady=20)
root.mainloop()
