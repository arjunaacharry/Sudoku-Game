import random

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid_move(board, row, col, num):
    if num in board[row] or num in [board[i][col] for i in range(4)]:
        return False

    start_row, start_col = 2 * (row // 2), 2 * (col // 2)
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if board[i][j] == num:
                return False

    return True

def is_board_full(board):
    for row in board:
        if 0 in row:
            return False
    return True

def play_sudoku():
    board = generate_sudoku()
    
    while not is_board_full(board):
        print("Current Sudoku Board:")
        print_board(board)

        try:
            row = int(input("Enter row number (1-4): ")) - 1
            col = int(input("Enter column number (1-4): ")) - 1
            num = int(input("Enter a number (1-4): "))

            if 0 <= row < 4 and 0 <= col < 4 and 1 <= num <= 4 and board[row][col] == 0 and is_valid_move(board, row, col, num):
                board[row][col] = num
            else:
                print("Invalid move. Try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("Congratulations! You've solved the Sudoku puzzle.")
    print("Final Sudoku Board:")
    print_board(board)

def generate_sudoku():
    board = [[0] * 4 for _ in range(4)]
    solve_sudoku(board)

    for _ in range(6):
        row, col = random.randint(0, 3), random.randint(0, 3)
        while board[row][col] == 0:
            row, col = random.randint(0, 3), random.randint(0, 3)
        board[row][col] = 0

    return board

def solve_sudoku(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                for num in range(1, 5):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

if __name__ == "__main__":
    print("Welcome to the 4x4 Sudoku Game!")
    play_sudoku()
