import random
import tkinter as tk
from tkinter import simpledialog, messagebox

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Game")
        self.board = generate_sudoku()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=450, height=450)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.cell_click)

        for i in range(9):
            for j in range(9):
                self.canvas.create_rectangle(
                    j * 50, i * 50, (j + 1) * 50, (i + 1) * 50, fill="white", outline="black"
                )
                num = self.board[i][j]
                if num != 0:
                    self.canvas.create_text(
                        (j + 0.5) * 50, (i + 0.5) * 50, text=str(num), font=("Helvetica", 16)
                    )

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_solution)
        self.submit_button.pack()

    def cell_click(self, event):
        col, row = int(event.x / 50), int(event.y / 50)
        num = simpledialog.askinteger("Input", "Enter a number (1-9):", parent=self.master)

        if num and 1 <= num <= 9 and is_valid_move(self.board, row, col, num):
            self.board[row][col] = num
            self.canvas.create_text(
                (col + 0.5) * 50, (row + 0.5) * 50, text=str(num), font=("Helvetica", 16)
            )
        else:
            messagebox.showwarning("Invalid Move", "Please enter a valid number.")

    def check_solution(self):
        if is_board_full(self.board):
            messagebox.showinfo("Congratulations!", "You've solved the Sudoku puzzle.")
        else:
            messagebox.showerror("Incomplete Sudoku", "Please complete the entire board.")

def is_valid_move(board, row, col, num):
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def is_board_full(board):
    for row in board:
        if 0 in row:
            return False
    return True

def generate_sudoku():
    board = [[0] * 9 for _ in range(9)]
    solve_sudoku(board)

    for _ in range(20):  # Adjust the number of cells to be empty based on the board size
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0

    return board

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
