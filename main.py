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
        self.num_guesses = 0
        self.max_guesses = 5

        self.canvas = tk.Canvas(self.root, width=400, height=300, bg="#f0f4f8", highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        self.shapes = []
        self.speeds = []
        colors = ["#FFB6C1", "#87CEFA", "#98FB98", "#FFD700"]
        for _ in range(6):
            x = random.randint(0, 380)
            y = random.randint(0, 280)
            size = random.randint(15, 25)
            color = random.choice(colors)
            shape = self.canvas.create_oval(x, y, x+size, y+size, fill=color, outline="")
            self.shapes.append(shape)
            self.speeds.append((random.choice([-1, 1]), random.choice([-1, 1])))

        self.animate_shapes()

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

    def animate_shapes(self):
        for i, shape in enumerate(self.shapes):
            dx, dy = self.speeds[i]
            self.canvas.move(shape, dx, dy)
            x0, y0, x1, y1 = self.canvas.coords(shape)
            if x0 <= 0 or x1 >= 400:
                dx *= -1
            if y0 <= 0 or y1 >= 300:
                dy *= -1
            self.speeds[i] = (dx, dy)
        self.root.after(30, self.animate_shapes)   

    def check_guess(self):
        guess = self.entry.get()
        self.num_guesses += 1

        if not guess.isdigit():
            self.result.config(text="❌ Please enter a number.")
            return

        guess = int(guess)

        if guess < self.secret:
            self.result.config(text="🔽 Too low!")
        elif guess > self.secret:
            self.result.config(text="🔼 Too high!")
        else:
            self.result.config(text=f"🎉 Correct! You guessed it in {self.num_guesses} tries.")
            self.button.config(state="disabled")
            self.entry.config(state="disabled")
            winsound.MessageBeep()
            return

        if self.num_guesses >= self.max_guesses:
            self.result.config(text=f"❌ Out of guesses! The number was {self.secret}.")
            self.button.config(state="disabled")
            self.entry.config(state="disabled")

    def reset_game(self):
        self.secret = random.randint(1, 100)
        self.num_guesses = 0
        self.result.config(text="")
        self.entry.delete(0, tk.END)
        self.button.config(state="normal")
        self.reset_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

