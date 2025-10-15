import random

points1 = 0
points2 = 0
flag = 0

# Define a dictionary to map choices to emojis
choices_emojis = {
    1: '🪨',  # Rock
    2: '✋',  # Paper
    3: '✂'   # Scissors
}

while flag < 3:
    print('Enter from the following choices:')
    print()
    choice1 = int(input("(1) for ROCK \n(2) for PAPER \n(3) for SCISSORS \n"))

    # Validate user input
    if choice1 not in choices_emojis:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue # Skip the rest of the loop and ask for input again

    choice2 = random.randint(1, 3)

    player1_emoji = choices_emojis[choice1]
    player2_emoji = choices_emojis[choice2]

    print(f"Player 1: {player1_emoji}\tPlayer 2: {player2_emoji}")

    if choice1 == choice2:
        print("It's a tie!")
    elif (choice1 == 1 and choice2 == 3) or \
         (choice1 == 2 and choice2 == 1) or \
         (choice1 == 3 and choice2 == 2):
        points1 += 1
        print("Player 1 wins this round!")
    else:
        points2 += 1
        print("Player 2 wins this round!")
    
    print(f"Current Score: Player 1 - {points1}, Player 2 - {points2}\n")
    flag += 1
    
print("---")
print("Game Over!")
if points1 > points2:
    print(f"User won with {points1} points!!!")
elif points2 > points1:
    print(f"Computer won with {points2} points!!!")
else:
    print(f"It's a draw! Both players scored {points1} points!!!")
