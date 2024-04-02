import tkinter as tk
from tkinter import messagebox
import random
import os

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.random_number = random.randint(1, 100)
        self.guesses_remaining = 5

        self.label = tk.Label(master, text="Guess the number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Submit Guess", command=self.check_guess)
        self.button.pack()

        self.high_score = self.get_high_score()
        self.high_score_label = tk.Label(master, text=f"High Score: {self.high_score}")
        self.high_score_label.pack()

    def get_high_score(self):
        high_score = 0
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", "r") as file:
                high_score = int(file.read())
        return high_score

    def update_high_score(self, score):
        with open("high_score.txt", "w") as file:
            file.write(str(score))
        self.high_score_label.config(text=f"High Score: {score}")

    def check_guess(self):
        guess = self.entry.get()
        if guess.isdigit():
            guess = int(guess)
            if guess == self.random_number:
                messagebox.showinfo("Congratulations!", f"You guessed the correct number: {self.random_number}")
                if self.guesses_remaining < self.high_score or self.high_score == 0:
                    self.update_high_score(self.guesses_remaining)
                    messagebox.showinfo("New High Score!", f"Congratulations! You've set a new high score: {self.guesses_remaining}")
                self.master.quit()
            else:
                self.guesses_remaining -= 1
                if self.guesses_remaining == 0:
                    messagebox.showerror("Game Over", f"Sorry, you've run out of guesses. The correct number was: {self.random_number}")
                    self.master.quit()
                else:
                    if guess < self.random_number:
                        messagebox.showinfo("Incorrect", f"Too low! You have {self.guesses_remaining} guesses remaining.")
                    else:
                        messagebox.showinfo("Incorrect", f"Too high! You have {self.guesses_remaining} guesses remaining.")
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid number between 1 and 100.")

def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
