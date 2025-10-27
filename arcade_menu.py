# arcade_menu.py

def arcade_menu():
    import hand_cricket, hangman, battleship, blackjack, typingspeed, rock_paper_scissors, tictactoe

    # Map menu numbers to game functions
    game_switch = {
        "1": hand_cricket.main,
        "2": hangman.main,            
        "3": battleship.battleship,
        "4": blackjack.play_blackjack,
        "5": typingspeed.typing_speed_game,
        "6": rock_paper_scissors.play_rps,
        "7": tictactoe.play_tictactoe
    }

    games = [
        "Hand Cricket",
        "Hangman",
        "Battleship",
        "Blackjack",
        "Typing Speed",
        "Rock Paper Scissors",
        "Tic Tac Toe"
    ]

    while True:
        print("\n===== Welcome to Python Arcade! =====\n")
        for idx, game in enumerate(games, start=1):
            print(f"{idx}. {game}")
        print("0. Exit Arcade")

        choice = input("\nEnter the number of the game you want to play: ").strip()

        if choice == "0":
            print("Thanks for playing! Goodbye!")
            break
        elif choice in game_switch:
            try:
                game_switch[choice]()  # Call the selected game
            except Exception as e:
                print(f"An error occurred while running the game: {e}")
        else:
            print("Invalid choice! Enter a number from 0 to 7.")

# Run the Arcade
if __name__ == "__main__":
    arcade_menu()
