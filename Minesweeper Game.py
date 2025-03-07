import random


def print_board(board):
    for row in board:
        print(" ".join(row))


def create_board(size, num_mines):
    board = [["." for _ in range(size)] for _ in range(size)]
    mines = set()

    while len(mines) < num_mines:
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        mines.add((row, col))

    for row, col in mines:
        board[row][col] = "*"

    return board, mines


def count_adjacent_mines(board, row, col):
    size = len(board)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < size and 0 <= c < size and board[r][c] == "*":
            count += 1
    return count


def reveal_board(board, mines):
    size = len(board)
    revealed = [["." for _ in range(size)] for _ in range(size)]

    for row in range(size):
        for col in range(size):
            if (row, col) in mines:
                revealed[row][col] = "*"
            else:
                revealed[row][col] = str(count_adjacent_mines(board, row, col))
    return revealed


def play_minesweeper():
    size = int(input("Enter the board size: "))
    num_mines = int(input("Enter the number of mines: "))

    board, mines = create_board(size, num_mines)
    revealed_board = [["." for _ in range(size)] for _ in range(size)]

    while True:
        print("\nCurrent Board:")
        print_board(revealed_board)

        try:
            row, col = map(int, input("Enter the row and column to reveal (e.g., 1 2): ").split())
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue

        if not (0 <= row < size and 0 <= col < size):
            print("Invalid position. Try again.")
            continue

        if (row, col) in mines:
            print("\nGame Over! You hit a mine.")
            print("Final Board:")
            print_board(reveal_board(board, mines))
            break

        revealed_board[row][col] = str(count_adjacent_mines(board, row, col))

        if all(revealed_board[r][c] != "." for r in range(size) for c in range(size) if (r, c) not in mines):
            print("\nCongratulations! You cleared the board.")
            print("Final Board:")
            print_board(reveal_board(board, mines))
            break


if __name__ == "__main__":
    play_minesweeper()
