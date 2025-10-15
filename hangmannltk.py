import numpy as np
import pandas as pd
import nltk
from nltk.corpus import words




word_list = words.words()

filtered_words = [w.lower() for w in word_list if 4 <= len(w) <= 10]
words = np.array(filtered_words)

# ---- PLAYER SETUP ----
name = input("Enter your name: ")   # takes player's name as input
print("Welcome to Hangman,", name)

rounds = 3              # total no. of rounds to be played 
overall = []            # to store each round's summary
wins = 0                # counter for total rounds won

# ---- GAME LOOP FOR EACH ROUND ----
for r in range(1, rounds + 1):
    print("\n----- Round", r, "-----")

    word = np.random.choice(words)       # pick random word
    display = np.array(["_"] * len(word))
    lives = 6
    guessed = []
    record = []

    print("The word has", len(word), "letters")

    # ---- ROUND LOOP ----
    while lives > 0 and "_" in display:
        guess = input("Enter a letter: ").lower().strip()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed:
            print("You already guessed that!")
            continue

        guessed.append(guess)

        if guess in word:
            print("✅ Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            lives -= 1
            print("❌ Wrong guess!")

        # show current progress
        word_show = " ".join(display)
        print("Word:", word_show)
        print("Lives left:", lives)
        print("Guessed letters:", guessed)

        # record progress for scoreboard
        record.append([len(record) + 1, guess, word_show, lives])

    # ---- ROUND RESULT ----
    if "_" not in display:
        print("🎉 Congrats", name + "! You guessed the word:", word)
        result = "Won"
        wins += 1
    else:
        print("💀 Sorry", name + ", you lost! The word was:", word)
        result = "Lost"

    # round scoreboard
    df = pd.DataFrame(record, columns=["Attempt", "Guessed Letter", "Word Progress", "Lives Left"])
    print("\nRound", r, "Scoreboard:\n")
    print(df)

    overall.append([r, word, result, 6 - lives])

# ---- FINAL SUMMARY ----
overall_arr = np.array(overall)
summary = pd.DataFrame(overall_arr, columns=["Round", "Word", "Result", "Wrong Guesses"])

print("\n===== FINAL GAME SUMMARY =====\n")
print(summary)

# ---- WINNER ANNOUNCEMENT ----
print("\n===== FINAL RESULT =====")
if wins > rounds / 2:
    print("🏆", name, "wins the game with", wins, "out of", rounds, "rounds!")
elif wins == rounds / 2:
    print("🤝 It's a tie! You won", wins, "rounds.")
else:
    print("💀", name, "lost the game. Better luck next time!")
