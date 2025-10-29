import winsound
import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guessing Game")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f4f8")

        self.secret = random.randint(1, 100)
        self.attempts = 0

        self.title_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14), bg="#f0f4f8")
        self.title_label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 12), justify="center")
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
        self.button.pack(pady=10)

        self.result = tk.Label(root, text="", font=("Arial", 12), bg="#f0f4f8")
        self.result.pack(pady=10)

        self.reset_button = tk.Button(root, text="Play Again", command=self.reset_game, font=("Arial", 10), bg="#2196F3", fg="white")
        self.reset_button.pack(pady=10)
        self.reset_button.config(state="disabled")

    def check_guess(self):
        guess = self.entry.get()
        self.attempts += 1
        if not guess.isdigit():
            self.result.config(text="⛔ Please enter a number.")
            return

        guess = int(guess)
        if guess < self.secret:
            self.result.config(text="🔻 Too low!")
        elif guess > self.secret:
            self.result.config(text="🔺 Too high!")
        else:
            self.result.config(text=f"🎉 Correct! Attempts: {self.attempts}")
            winsound.MessageBeep()
            messagebox.showinfo("You won!", f" you guessed it in {self.attempts} attempts!")
            self.button.config(state="disabled")
            self.reset_button.config(state="normal")

    def reset_game(self):
        self.secret = random.randint(1, 100)
        self.attempts = 0
        self.result.config(text="")
        self.entry.delete(0, tk.END)
        self.button.config(state="normal")
        self.reset_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

