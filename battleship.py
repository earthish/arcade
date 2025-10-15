import random
import time

def print_board(board):
    """Displays the current game board."""
    for row in board:
        print(" ".join(row))
    print()

def create_board(size):
    """Creates an empty game board."""
    return [["~"] * size for _ in range(size)]

def random_ship_positions(size, num_ships):
    """Places ships randomly on the board."""
    ships = set()
    while len(ships) < num_ships:
        ships.add((random.randint(0, size - 1), random.randint(0, size - 1)))
    return ships

def battleship():
    print("\n🚢 Welcome to Mini Battleship!")
    print("Try to sink all the computer's ships!\n")
    time.sleep(1)

    size = 5  # 5x5 grid
    num_ships = 3
    turns = 8  # limited tries

    board = create_board(size)
    ships = random_ship_positions(size, num_ships)
    hits = set()

    print_board(board)

    for turn in range(1, turns + 1):
        print(f"Turn {turn} of {turns}")
        try:
            row = int(input(f"Enter row (0-{size-1}): "))
            col = int(input(f"Enter col (0-{size-1}): "))
        except ValueError:
            print("Invalid input. Enter numbers only!")
            continue

        if (row, col) in hits:
            print("You already tried that spot!")
            continue

        if (row, col) in ships:
            print("💥 Hit!")
            board[row][col] = "X"
            hits.add((row, col))
            if hits == ships:
                print_board(board)
                print("\n🏆 You sunk all the ships! You win!")
                return
        else:
            print("🌊 Miss!")
            board[row][col] = "O"
            hits.add((row, col))

        print_board(board)
        time.sleep(0.5)

    print("\n💀 Game Over!")
    print(f"The ships were at: {ships}")

# --- Run the Game ---
if __name__ == "__main__":
    battleship()
