import numpy as np
import random

def create_board():
    """Step 1: Create a 3x3 matrix"""
    return np.full((3, 3), ' ')

def print_board(board):
    """Step 4: Print the board"""
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print("\n")

def check_win(board, symbol):
    """Step 5: Check win condition"""
    # Check rows and columns
    for i in range(3):
        if all(board[i, :] == symbol) or all(board[:, i] == symbol):
            return True
    # Check diagonals
    if all(np.diag(board) == symbol) or all(np.diag(np.fliplr(board)) == symbol):
        return True
    return False

def available_moves(board):
    """Return list of available (row, col) moves"""
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i, j] == ' ':
                moves.append((i, j))
    return moves

def computer_move(board, comp_symbol, user_symbol):
    """Step 6: Computer's logic for choosing a move"""
    moves = available_moves(board)

    # ⿡ Try to win if possible
    for (i, j) in moves:
        temp = board.copy()
        temp[i, j] = comp_symbol
        if check_win(temp, comp_symbol):
            return (i, j)

    # ⿢ Try to block user’s winning move
    for (i, j) in moves:
        temp = board.copy()
        temp[i, j] = user_symbol
        if check_win(temp, user_symbol):
            return (i, j)

    # ⿣ Check for 2 same symbols in rows or cols or diagonals and complete
    # --- Rows ---
    for i in range(3):
        row = board[i]
        if list(row).count(comp_symbol) == 2 and ' ' in row:
            j = list(row).index(' ')
            return (i, j)

    # --- Columns ---
    for j in range(3):
        col = board[:, j]
        if list(col).count(comp_symbol) == 2 and ' ' in col:
            i = list(col).index(' ')
            return (i, j)

    # --- Diagonals ---
    diag1 = [board[i, i] for i in range(3)]
    if diag1.count(comp_symbol) == 2 and ' ' in diag1:
        idx = diag1.index(' ')
        return (idx, idx)

    diag2 = [board[i, 2 - i] for i in range(3)]
    if diag2.count(comp_symbol) == 2 and ' ' in diag2:
        idx = diag2.index(' ')
        return (idx, 2 - idx)

    # ⿤ Otherwise pick random from remaining available
    return random.choice(moves) if moves else None

def play_game():
    scoreboard = {"User": 0, "Computer": 0}

    while True:
        board = create_board()
        print("Welcome to Tic Tac Toe!\n")

        # Step 2: User details
        user_name = input("Enter your name: ").strip()
        user_symbol = input("Choose your symbol (X or O): ").upper()
        while user_symbol not in ['X', 'O']:
            user_symbol = input("Invalid! Choose X or O: ").upper()

        comp_symbol = 'O' if user_symbol == 'X' else 'X'

        print(f"\n{user_name} is '{user_symbol}'  |  Computer is '{comp_symbol}'")
        print_board(board)

        turn = random.choice(['User', 'Computer'])
        print(f"{turn} will start!\n")

        for _ in range(9):  # maximum 9 moves
            if turn == 'User':
                print(f"{user_name}'s turn:")
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter column (0-2): "))
                except ValueError:
                    print("Invalid input! Try again.")
                    continue

                if 0 <= row < 3 and 0 <= col < 3 and board[row, col] == ' ':
                    board[row, col] = user_symbol
                else:
                    print("Invalid move! Cell already taken or out of range.")
                    continue

                print_board(board)

                if check_win(board, user_symbol):
                    print(f"🎉 {user_name} won!")
                    scoreboard["User"] += 1
                    break
                turn = 'Computer'

            else:
                print("Computer's turn...")
                move = computer_move(board, comp_symbol, user_symbol)
                if move:
                    board[move] = comp_symbol
                    print_board(board)

                    if check_win(board, comp_symbol):
                        print("💻 Computer won!")
                        scoreboard["Computer"] += 1
                        break
                turn = 'User'
        else:
            print("It's a tie!")

        print("\n📊 Scoreboard:")
        print(f"{user_name}: {scoreboard['User']} | Computer: {scoreboard['Computer']}")

        # Replay option
        cont = input("\nDo you want to play again? (yes/no): ").lower()
        if cont != 'yes':
            print("\nThanks for playing! Final Scoreboard:")
            print(f"{user_name}: {scoreboard['User']} | Computer: {scoreboard['Computer']}")
            break

# Run the game
play_game()