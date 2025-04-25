# File: 120140086_Quiz.py
# Author: Reza Chairul Manam
# NIM: 120140086
# Class: Praktikum PBO-RC
#===================================================================================================
# Quiz:

import random

class Cell:
    def __init__(self):
        self.is_bomb = False
        self.revealed = False

    def reveal(self):
        self.revealed = True

    def display(self):
        if self.revealed:
            return "X" if self.is_bomb else "O"
        else:
            return "?"

class Minesweeper:
    def __init__(self, rows=3, cols=3):
        self.rows = rows
        self.cols = cols
        self.board = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.bomb_row = random.randint(0, rows - 1)
        self.bomb_col = random.randint(0, cols - 1)
        self.board[self.bomb_row][self.bomb_col].is_bomb = True
        self.game_over = False

    def print_board(self):
        print("=" * 40)
        for row in self.board:
            print(" ".join(cell.display() for cell in row))
        print("=" * 40)

    def play_turn(self, row, col):
        if self.board[row][col].revealed:
            print("Kotak ini sudah dibuka.")
            return

        self.board[row][col].reveal()
        if self.board[row][col].is_bomb:
            self.game_over = True
            self.print_board()
            print("Boom! Kamu kalah!")
        else:
            print("Tidak ada bom di sini. Lanjutkan!")
            if self.check_win():
                self.print_board()
                print("Selamat! Kamu menang!")

    def check_win(self):
        for row in self.board:
            for cell in row:
                if not cell.is_bomb and not cell.revealed:
                    return False
        self.game_over = True
        return True

    def run(self):
        while not self.game_over:
            self.print_board()
            try:
                row = int(input("Masukkan baris (0-2): "))
                col = int(input("Masukkan kolom (0-2): "))
                if 0 <= row < self.rows and 0 <= col < self.cols:
                    self.play_turn(row, col)
                else:
                    print("Koordinat tidak valid.")
            except ValueError:
                print("Masukkan angka yang valid.")

# Jalankan game
game = Minesweeper()
game.run()
