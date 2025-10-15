import random
import time

# --- Helper Functions ---

def get_valid_input(prompt, value_type=int, min_value=None, max_value=None):
    """Get valid integer input within an optional range."""
    while True:
        try:
            user_input = value_type(input(prompt))
            # Check for minimum value
            if min_value is not None and user_input < min_value:
                print(f"Please enter a value of at least {min_value}.")
                continue
            # Check for maximum value
            if max_value is not None and user_input > max_value:
                print(f"Please enter a value of at most {max_value}.")
                continue
            
            # Check for range if both min and max are set
            if (min_value is not None and max_value is not None and 
                (user_input < min_value or user_input > max_value)):
                 print(f"Please enter a value between {min_value} and {max_value}.")
                 continue
                 
            return user_input
        except ValueError:
            print("Invalid input. Please enter a number.")

# --- Game Setup ---

def get_game_settings():
    """Get desired number of wickets and overs."""
    print("\n--- Game Setup ---")
    # Using the improved input function for settings
    wickets = get_valid_input("Enter number of wickets (e.g., 1-10): ", min_value=1)
    overs = get_valid_input("Enter number of overs (e.g., 1-10): ", min_value=1)
    return wickets, overs

# --- Toss Logic ---

def toss():
    """Handles the toss: user chooses odd/even and plays against the computer."""
    print("\n--- Toss Time (Odd or Even) ---")
    
    # 1. User chooses Odd or Even
    while True:
        choice_input = input("Choose 'odd' or 'even': ").strip().lower()
        if choice_input in ['odd', 'o']:
            player_choice = 'odd'
            break
        elif choice_input in ['even', 'e']:
            player_choice = 'even'
            break
        print("Invalid choice. Please type 'odd' or 'even'.")

    # Determine Computer's choice
    computer_choice = 'even' if player_choice == 'odd' else 'odd'
    print(f"You chose {player_choice.upper()}, Computer gets {computer_choice.upper()}.")
    
    # 2. Both choose number 0–6
    player_num = get_valid_input("Enter your number for the toss (0–6): ", min_value=0, max_value=6)
    computer_num = random.randint(0, 6)
    
    print(f"You showed: {player_num}")
    print(f"Computer showed: {computer_num}")
    time.sleep(1)

    # 3. Calculate sum and decide winner
    total_sum = player_num + computer_num
    toss_result = 'odd' if total_sum % 2 != 0 else 'even'
    print(f"The sum is {total_sum}, which is {toss_result.upper()}.")

    # 4. Decide winner and choice
    if toss_result == player_choice:
        print("🎉 You win the toss!")
        toss_winner = "Player"
        while True:
            choice = input("Choose 'bat' or 'bowl': ").strip().lower()
            if choice in ['bat', 'b']:
                return toss_winner, "bat"
            elif choice in ['bowl', 'w']:
                return toss_winner, "bowl"
            print("Invalid choice. Please type 'bat' or 'bowl'.")
    else:
        print("💻 Computer wins the toss!")
        toss_winner = "Computer"
        # Computer chooses randomly to bat or bowl
        comp_choice = random.choice(['bat', 'bowl'])
        print(f"Computer chooses to {comp_choice.upper()} first.")
        return toss_winner, comp_choice

# --- Innings Logic ---

def run_innings(batting_team, bowling_team, max_wickets, max_overs, target=None):
    """
    Simulates one innings of Hand Cricket.
    Runs until max_wickets are lost, max_overs are completed, or the target is reached.
    """
    current_runs = 0
    wickets_lost = 0
    balls_bowled = 0
    max_balls = max_overs * 6
    
    # Helper for player input (Bat or Bowl move, 1-6)
    def get_player_move():
        """Get the player's run/bowl number (1-6)."""
        return get_valid_input("Enter your move (1-6): ", min_value=1, max_value=6)
    
    # Helper for computer move (Bat or Bowl move, 1-6)
    def get_computer_move():
        """Get the computer's run/bowl number (1-6)."""
        # Computer's move is a random number from 1 to 6
        return random.randint(1, 6)

    print(f"\n{batting_team} is Batting | {bowling_team} is Bowling.")
    if target is not None:
        print(f"Target is {target} runs.")

    # Main game loop: plays until out, overs run out, or target reached
    while wickets_lost < max_wickets and balls_bowled < max_balls:
        
        # Display current status header
        print("-" * 35)
        current_over = balls_bowled // 6
        current_ball = balls_bowled % 6 + 1 # Display as 1-6 balls
        
        score_line = f"Score: {current_runs}/{wickets_lost} | Over: {current_over}.{current_ball} ({balls_bowled + 1} of {max_balls})"
        
        # Display runs needed for the chasing team
        if target is not None:
            runs_needed = target - current_runs
            score_line += f" | Needs: {runs_needed} to win"
            # If target reached, break before playing the ball
            if runs_needed <= 0:
                 break 
        
        print(score_line)
        
        # Get moves from the batter and bowler
        try:
            if batting_team == "Player":
                batter_num = get_player_move()
                bowler_num = get_computer_move()
                print(f"You Batted: {batter_num} | Computer Bowled: {bowler_num}")
            else: # Computer is Batting
                bowler_num = get_player_move()
                batter_num = get_computer_move()
                print(f"Computer Batted: {batter_num} | You Bowled: {bowler_num}")
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting.")
            return current_runs, balls_bowled # Return current score on interruption

        # Check for OUT (Moves match)
        if batter_num == bowler_num:
            print("🚨 OUT! Both players played the same number.")
            wickets_lost += 1
            print(f"Wickets remaining: {max_wickets - wickets_lost}")
        else:
            runs_scored = batter_num
            current_runs += runs_scored
            print(f"💰 {batting_team} scores {runs_scored} runs!")
        
        balls_bowled += 1
        time.sleep(0.5)

        # Check for target reached immediately after scoring
        if target is not None and current_runs >= target:
            print(f"\n🎉 {batting_team} reached the target of {target - 1}!")
            break

    # Innings ends due to wickets, overs, or target reached
    print("\n" + "=" * 40)
    print(f"--- {batting_team.upper()} INNINGS ENDED ---")
    print(f"Final Score: {current_runs}/{wickets_lost} in {balls_bowled // 6}.{balls_bowled % 6} Overs.")
    print("=" * 40)
    return current_runs, balls_bowled

def game_result(score1, score2, target, batting_first, batting_second):
    """Determines and prints the final result of the game."""
    
    print("\n\n--- FINAL RESULT ---")
    
    if score2 >= target:
        # Batting second won
        winner = batting_second
        # Target is score1 + 1. If score2 >= target, second team won.
        print(f"\n🎉 WINNER: {winner.upper()}!")
        print(f"{winner} wins the match by scoring {score2} runs (Target: {target}).")
    elif score2 < score1:
        # Batting first won
        winner = batting_first
        runs_difference = score1 - score2
        print(f"\n🏆 WINNER: {winner.upper()}!")
        print(f"{winner} won by {runs_difference} runs.")
    else: # score1 == score2
        print("\n🤝 DRAW! The match is tied.")
    
    print("\nThanks for playing Python Hand Cricket!")

# --- Main Game Loop ---

def main():
    """Main function to run the Hand Cricket Game."""
    print("🏏 Welcome to Python Hand Cricket!")
    
    # 1. Game setup
    wickets, overs = get_game_settings()
    total_balls = overs * 6
    print(f"\nGame set: {wickets} Wickets, {overs} Overs ({total_balls} balls total).")
    
    # 2. Toss
    toss_winner, first_choice = toss()
    
    # Determine Batting Order
    if first_choice == 'bat':
        batting_first = toss_winner
    else:
        batting_first = 'Computer' if toss_winner == 'Player' else 'Player'
    batting_second = 'Computer' if batting_first == 'Player' else 'Player'
    
    print("\n--- Match Details ---")
    print(f"1st Innings: {batting_first} BATS")
    print(f"2nd Innings: {batting_second} BATS")
    
    # 3. First Innings (Sets the target)
    print(f"\n========================================\n  {batting_first.upper()} BATTING (INNINGS 1) \n========================================")
    
    first_innings_score, balls_played_1 = run_innings(
        batting_team=batting_first,
        bowling_team=batting_second,
        max_wickets=wickets,
        max_overs=overs,
        target=None # No target in the first innings
    )
    
    target = first_innings_score + 1
    
    # 4. Second Innings (Chase the target)
    print(f"\n========================================\n  {batting_second.upper()} BATTING (INNINGS 2) \n  Target: {target} runs to win. \n========================================")
    
    second_innings_score, balls_played_2 = run_innings(
        batting_team=batting_second,
        bowling_team=batting_first,
        max_wickets=wickets,
        max_overs=overs,
        target=target
    )
    
    # 5. Determine Result
    game_result(first_innings_score, second_innings_score, target, batting_first, batting_second)


if __name__ == "__main__":
    main()
