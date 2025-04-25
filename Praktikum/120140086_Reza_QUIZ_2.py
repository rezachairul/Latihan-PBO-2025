# File: 120140086_Quiz_2.py
# Author: Reza Chairul Manam
# NIM: 120140086
# Class: Praktikum PBO-RC
#===================================================================================================
# Quiz 2:
import random

class Hangman:
    def __init__(self, word_list, attempts=6):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.attempts_left = attempts
        self.guessed_letters = []
        self.correct_letters = ['_' for _ in self.word]

    def display_hangman(self):
        stages = [
            """
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
               |   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
                   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
                   |
                   |
                   |
                   |
            =========
            """
        ]
        print(stages[6 - self.attempts_left])

    def play(self):
        print("Welcome to Hangman!")

        while self.attempts_left > 0 and '_' in self.correct_letters:
            print("\nThe word is:", ''.join(self.correct_letters))
            guess = input("Guess a letter: ").lower()

            if guess in self.guessed_letters:
                print("You already guessed that letter.")
                continue

            self.guessed_letters.append(guess)

            if guess in self.word:
                print("Correct!")
                for idx, letter in enumerate(self.word):
                    if letter == guess:
                        self.correct_letters[idx] = guess
            else:
                self.attempts_left -= 1
                print(f"Incorrect. You have {self.attempts_left} attempts left.")
                self.display_hangman()

        if '_' not in self.correct_letters:
            print("\nCongratulations! You guessed the word:", self.word)
        else:
            self.display_hangman()
            print("\nGame Over! The word was:", self.word)


# Daftar kata
word_list = ['java', 'python', 'jumbo', 'joker', 'apple']

# Mulai game
game = Hangman(word_list)
game.play()
