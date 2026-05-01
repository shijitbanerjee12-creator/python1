import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("400x400")

        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0
        tk.Label(root, text="Rock Paper Scissors",
                 font=("Arial", 18, "bold")).pack(pady=10)
        self.result_label = tk.Label(root, text="Choose your move!",
                                     font=("Arial", 12))
        self.result_label.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Rock", width=10,
                  command=lambda: self.play("Rock")).grid(row=0, column=0, padx=5)

        tk.Button(button_frame, text="Paper", width=10,
                  command=lambda: self.play("Paper")).grid(row=0, column=1, padx=5)

        tk.Button(button_frame, text="Scissors", width=10,
                  command=lambda: self.play("Scissors")).grid(row=0, column=2, padx=5)
        self.user_choice_label = tk.Label(root, text="Your Choice: ",
                                         font=("Arial", 11))
        self.user_choice_label.pack(pady=5)

        self.comp_choice_label = tk.Label(root, text="Computer Choice: ",
                                         font=("Arial", 11))
        self.comp_choice_label.pack(pady=5)
        self.score_label = tk.Label(root,
                                   text="Score - You: 0 | Computer: 0",
                                   font=("Arial", 12, "bold"))
        self.score_label.pack(pady=10)
        tk.Button(root, text="Reset Game", command=self.reset_game).pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        self.user_choice_label.config(text=f"Your Choice: {user_choice}")
        self.comp_choice_label.config(text=f"Computer Choice: {computer_choice}")
        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Win!"
            self.user_score += 1
        else:
            result = "Computer Wins!"
            self.computer_score += 1
        self.result_label.config(text=result)
        self.score_label.config(
            text=f"Score - You: {self.user_score} | Computer: {self.computer_score}"
        )

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="Choose your move!")
        self.user_choice_label.config(text="Your Choice: ")
        self.comp_choice_label.config(text="Computer Choice: ")
        self.score_label.config(text="Score - You: 0 | Computer: 0")
        messagebox.showinfo("Reset", "Game has been reset!")
if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()