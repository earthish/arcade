import random
import time

# Optional: use pandas for pretty round scoreboards if available
try:
    import pandas as pd
    _HAS_PANDAS = True
except Exception:
    _HAS_PANDAS = False

# Try to use NLTK words if available; otherwise fall back to a small built-in list.
try:
    import nltk
    from nltk.corpus import words as nltk_words
    # try to access the corpus; this may raise LookupError if not downloaded
    word_list_source = [w.lower() for w in nltk_words.words() if 4 <= len(w) <= 10]
    if not word_list_source:
        raise LookupError  # fallback if corpus empty
except Exception:
    # fallback word list (simple, safe)
    word_list_source = [
        "apple", "banana", "cherry", "dragon", "forest", "garden", "hacker",
        "island", "jungle", "kettle", "library", "mountain", "nectar",
        "ocean", "puzzle", "rocket", "silver", "turkey", "umbrella", "violet"
    ]

# Ensure all words are lowercase and unique
WORDS = list({w.lower() for w in word_list_source if 4 <= len(w) <= 10})


def play_round(secret_word, max_lives=6):
    """Play a single round of hangman. Returns (won_bool, wrong_guesses_count, record_list)."""
    word = secret_word.lower()
    display = ["_"] * len(word)
    lives = max_lives
    guessed = set()
    record = []  # rows: [attempt_no, guessed_letter, word_progress, lives_left]

    attempt_no = 0
    while lives > 0 and "_" in display:
        attempt_no += 1
        print("\nWord:", " ".join(display))
        print(f"Lives left: {lives} | Guessed: {sorted(list(guessed))}")
        guess = input("Enter a letter: ").lower().strip()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter.")
            attempt_no -= 1
            continue

        if guess in guessed:
            print("You already guessed that!")
            attempt_no -= 1
            continue

        guessed.add(guess)

        if guess in word:
            print("✅ Good guess!")
            for i, ch in enumerate(word):
                if ch == guess:
                    display[i] = guess
        else:
            lives -= 1
            print("❌ Wrong guess!")

        record.append([attempt_no, guess, " ".join(display), lives])

    won = "_" not in display
    wrong_guesses = max_lives - lives
    return won, wrong_guesses, record, word


def main():
    print("🎯 Welcome to Hangman!")
    name = input("Enter your name: ").strip() or "Player"

    # number of rounds: can be adjusted
    rounds = 3
    wins = 0
    overall = []  # list of [round_no, word, result, wrong_guesses]

    for r in range(1, rounds + 1):
        print(f"\n----- Round {r} -----")
        secret = random.choice(WORDS)
        print(f"(Hint: the word has {len(secret)} letters)")

        won, wrong_guesses, record, word = play_round(secret, max_lives=6)

        if won:
            print(f"\n🎉 Congrats {name}! You guessed the word: {word}")
            result = "Won"
            wins += 1
        else:
            print(f"\n💀 Sorry {name}, you lost! The word was: {word}")
            result = "Lost"

        # Show round scoreboard (use pandas if available)
        print(f"\nRound {r} Scoreboard:\n")
        if _HAS_PANDAS and record:
            df = pd.DataFrame(record, columns=["Attempt", "Guessed Letter", "Word Progress", "Lives Left"])
            print(df.to_string(index=False))
        else:
            if record:
                print(f"{'Attempt':>7} | {'Guess':>5} | {'Progress':>20} | {'Lives':>5}")
                print("-" * 50)
                for row in record:
                    print(f"{row[0]:7} | {row[1]:5} | {row[2]:20} | {row[3]:5}")
            else:
                print("(No attempts were made.)")

        overall.append([r, word, result, wrong_guesses])

    # Final summary (use pandas if available)
    print("\n===== FINAL GAME SUMMARY =====\n")
    if _HAS_PANDAS and overall:
        summary_df = pd.DataFrame(overall, columns=["Round", "Word", "Result", "Wrong Guesses"])
        print(summary_df.to_string(index=False))
    else:
        print(f"{'Round':>5} | {'Word':>10} | {'Result':>6} | {'Wrong':>6}")
        print("-" * 40)
        for row in overall:
            print(f"{row[0]:5} | {row[1]:10} | {row[2]:6} | {row[3]:6}")

    # Winner announcement (tie logic fixed)
    print("\n===== FINAL RESULT =====")
    if wins * 2 > rounds:
        print("🏆", name, "wins the game with", wins, "out of", rounds, "rounds!")
    elif wins * 2 == rounds:
        print("🤝 It's a tie! You won", wins, "rounds.1")
    else:
        print("💀", name, "lost the game. Better luck next time!")

    input("\nPress Enter to return to the Arcade Menu...")


if __name__ == "__main__":
    main()
