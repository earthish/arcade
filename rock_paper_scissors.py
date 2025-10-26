import random

def play_rps():
    points1 = 0
    points2 = 0
    rounds_played = 0
    total_rounds = 3  # You can change this if you want more rounds

    # Map choices to emojis
    choices_emojis = {
        1: '🪨',  # Rock
        2: '✋',  # Paper
        3: '✂'   # Scissors
    }

    while rounds_played < total_rounds:
        print("\nEnter from the following choices:")
        try:
            choice1 = int(input("(1) for ROCK \n(2) for PAPER \n(3) for SCISSORS \n"))
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")
            continue

        # Validate input
        if choice1 not in choices_emojis:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        choice2 = random.randint(1, 3)

        print(f"Player: {choices_emojis[choice1]}  |  Computer: {choices_emojis[choice2]}")

        if choice1 == choice2:
            print("It's a tie!")
        elif (choice1 == 1 and choice2 == 3) or \
             (choice1 == 2 and choice2 == 1) or \
             (choice1 == 3 and choice2 == 2):
            points1 += 1
            print("You win this round!")
        else:
            points2 += 1
            print("Computer wins this round!")

        print(f"Current Score: You - {points1}, Computer - {points2}")
        rounds_played += 1

    # --- Game Over ---
    print("\n--- Game Over ---")
    if points1 > points2:
        print(f"🏆 You won with {points1} points!")
    elif points2 > points1:
        print(f"💻 Computer won with {points2} points!")
    else:
        print(f"🤝 It's a draw! Both scored {points1} points!")

    input("\nPress Enter to return to the Arcade Menu...")

# --- Run standalone ---
if __name__ == "__main__":
    play_rps()
