import random
import time

def print_board(board):
    """Displays the current board."""
    for row in board:
        print(" ".join(row))
    print()

def create_board(size):
    """Creates an empty board of given size."""
    return [["~"] * size for _ in range(size)]

def random_ship_positions(size, num_ships):
    """Randomly generates ship coordinates."""
    ships = set()
    while len(ships) < num_ships:
        ships.add((random.randint(0, size - 1), random.randint(0, size - 1)))
    return ships

def battleship():
    """Main game function."""
    print("\n🚢 Welcome to Mini Battleship!")
    print("Try to sink all the computer's ships!\n")
    time.sleep(1)

    size = 5          # board size (5x5)
    num_ships = 3     # number of ships
    turns = 8         # total turns

    board = create_board(size)
    ships = random_ship_positions(size, num_ships)
    hits = set()

    print_board(board)

    for turn in range(1, turns + 1):
        print(f"Turn {turn} of {turns}")

        # user input with validation
        try:
            row = int(input(f"Enter row (0-{size-1}): "))
            col = int(input(f"Enter col (0-{size-1}): "))
        except ValueError:
            print("Invalid input. Enter numbers only!")
            continue

        if not (0 <= row < size and 0 <= col < size):
            print(f"Coordinates must be between 0 and {size-1}. Try again.")
            continue

        if (row, col) in hits:
            print("You already tried that spot!")
            continue

        # check hit/miss
        if (row, col) in ships:
            print("💥 Hit!")
            board[row][col] = "X"
            hits.add((row, col))

            if hits == ships:
                print_board(board)
                print("\n🏆 You sunk all the ships! You win!")
                input("\nPress Enter to return to the Arcade Menu...")
                return
        else:
            print("🌊 Miss!")
            board[row][col] = "O"
            hits.add((row, col))

        print_board(board)
        time.sleep(0.5)

    # Game over sequence
    print("\n💀 Game Over!")
    print("Here were the ships:")
    for (r, c) in ships:
        board[r][c] = "S"
    print_board(board)
    input("\nPress Enter to return to the Arcade Menu...")

def main():
    battleship()

if __name__ == "__main__":
    main()
