import numpy as np      
import pandas as pd     

# ---- PLAYER SETUP ----
name = input("Enter your name: ")   # takes player's name as input
print("Welcome to Hangman,", name)

# list of words stored as numpy array
words = np.array(["python", "computer", "science", "array", "hangman", "programming", "numpy", "pandas", "matplotlib"])

rounds = 3              # total no. of rounds to be played 
overall = []            # empty list to store the summary info of each round's results
wins = 0                # counter that counts the total no. of rounds won

# ---- GAME LOOP FOR EACH ROUND ----
for r in range(1, rounds + 1):
    print("\n----- Round", r, "-----")

    word = np.random.choice(words)       # picks a random word from the list of words(i.e secret word to be guessed by player)
    display = np.array(["_"] * len(word))  # display hidden letters as underscores
    lives = 6                             # total no. of chances to guess
    guessed = []                          # for storing the guessed letters to prevent repeated guess
    record = []                           # for storing each round's data (attempt,progress,lives left, etc)

    print("The word has", len(word), "letters")

    # ---- ROUND LOOP ----
    while lives > 0 and "_" in display:
        guess = input("Enter a letter: ").lower()  # takes input from player and converts it to lowercase

        if guess in guessed:       # checks if letter is already guessed before by the player
            print("You already guessed that!")
            continue               #skips rest of this loop and asks for next letter

        guessed.append(guess)      # adds the guessed letter by the player to the guessed list

        if guess in word:          # checks if guessed letter exists in the word or not
            print("Good guess!")
            for i in range(len(word)):   # reveal all positions of guessed letter
                if word[i] == guess:
                    display[i] = guess   #replace underscore at the same position with the guessed letter
        else:
            lives -= 1             # lose one life if guess is wrong
            print("Wrong guess!")

        # shows the current progress of word
        word_show = ""
        for ch in display:
            word_show += ch + " "     # add the character and a space to word_show(i.e player can see the progress of word)

        # printing game info after each guess
        print("Word:", word_show)
        print("Lives left:", lives)
        print("Guessed letters:", guessed)

        # record current state for DataFrame
        record.append([len(record) + 1, guess, word_show.strip(), lives])

    # ---- ROUND RESULT ----
    if "_" not in display:          # if the word is fully guessed by player
        print("Congrats", name, "! You guessed the word:", word)
        result = "Won"
        wins += 1
    else:
        print("Sorry", name, ", you lost! The word was:", word)
        result = "Lost"

    # creating DataFrame for this round
    df = pd.DataFrame(record, columns=["Attempt", "Guessed Letter", "Word Progress", "Lives Left"])
    print("\nRound", r, "Scoreboard:\n")
    print(df)

    # storing the round summary for final results
    overall.append([r, word, result, 6 - lives])

# ---- FINAL SUMMARY ----
overall_arr = np.array(overall)   # convert overall results to numpy array
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