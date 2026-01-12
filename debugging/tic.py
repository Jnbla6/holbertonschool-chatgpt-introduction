#!/usr/bin/python3
def print_board(board):
    """
    Function description:
    Prints the current state of the Tic-Tac-Toe board to the console.

    Parameters:
    board: A list of lists representing the 3x3 game grid.

    Returns:
    None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """
    Function description:
    Checks if there is a winning condition on the board (rows, columns, or diagonals).

    Parameters:
    board: A list of lists representing the 3x3 game grid.

    Returns:
    True if a winner is found, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """
    Function description:
    Checks if the board is full, resulting in a draw.

    Parameters:
    board: A list of lists representing the 3x3 game grid.

    Returns:
    True if the board is full and there is no winner, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Function description:
    Main game loop. Handles user input, updates the board, and manages turns.

    Parameters:
    None

    Returns:
    None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # Input validation loop
        while True:
            try:
                print(f"Player {player}'s turn.")
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))

                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board[row][col] == " ":
                        board[row][col] = player
                        break # Valid move, exit input loop
                    else:
                        print("That spot is already taken! Try again.")
                else:
                    print("Invalid coordinates! Please enter numbers between 0 and 2.")
            except ValueError:
                print("Invalid input! Please enter numeric values.")

        # Check for win immediately after the move
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        # Check for draw
        if check_draw(board):
            print_board(board)
            print("It's a Draw!")
            break

        # Swap player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()