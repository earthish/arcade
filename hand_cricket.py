import random
import time

# --- Helper Functions ---

def get_valid_input(prompt, value_type=int, min_value=None, max_value=None):
    """Get valid integer input within an optional range."""
    while True:
        try:
            user_input = value_type(input(prompt))
            if min_value is not None and user_input < min_value:
                print(f"Please enter a value of at least {min_value}.")
                continue
            if max_value is not None and user_input > max_value:
                print(f"Please enter a value of at most {max_value}.")
                continue
            return user_input
        except ValueError:
            print("Invalid input. Please enter a number.")

# --- Game Setup ---

def get_game_settings():
    """Get desired number of wickets and overs."""
    print("\n--- Game Setup ---")
    wickets = get_valid_input("Enter number of wickets (1–10): ", min_value=1)
    overs = get_valid_input("Enter number of overs (1–10): ", min_value=1)
    return wickets, overs

# --- Toss Logic ---

def toss():
    """Handles the toss: user chooses odd/even and plays against the computer."""
    print("\n--- Toss Time (Odd or Even) ---")
    
    while True:
        choice_input = input("Choose 'odd' or 'even': ").strip().lower()
        if choice_input in ['odd', 'o']:
            player_choice = 'odd'
            break
        elif choice_input in ['even', 'e']:
            player_choice = 'even'
            break
        print("Invalid choice. Please type 'odd' or 'even'.")

    computer_choice = 'even' if player_choice == 'odd' else 'odd'
    print(f"You chose {player_choice.upper()}, Computer gets {computer_choice.upper()}.")

    player_num = get_valid_input("Enter your number for the toss (0–6): ", min_value=0, max_value=6)
    computer_num = random.randint(0, 6)

    print(f"You showed: {player_num}")
    print(f"Computer showed: {computer_num}")
    time.sleep(1)

    total_sum = player_num + computer_num
    toss_result = 'odd' if total_sum % 2 != 0 else 'even'
    print(f"The sum is {total_sum}, which is {toss_result.upper()}.")

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
        comp_choice = random.choice(['bat', 'bowl'])
        print(f"Computer chooses to {comp_choice.upper()} first.")
        return toss_winner, comp_choice

# --- Innings Logic ---

def run_innings(batting_team, bowling_team, max_wickets, max_overs, target=None):
    """Simulates one innings of Hand Cricket."""
    current_runs = 0
    wickets_lost = 0
    balls_bowled = 0
    max_balls = max_overs * 6

    def get_player_move():
        return get_valid_input("Enter your move (1–6): ", min_value=1, max_value=6)

    def get_computer_move():
        return random.randint(1, 6)

    print(f"\n{batting_team} is Batting | {bowling_team} is Bowling.")
    if target is not None:
        print(f"Target: {target} runs")

    while wickets_lost < max_wickets and balls_bowled < max_balls:
        print("-" * 35)
        current_over = balls_bowled // 6
        current_ball = balls_bowled % 6 + 1
        score_line = f"Score: {current_runs}/{wickets_lost} | Over: {current_over}.{current_ball}"

        if target is not None:
            runs_needed = target - current_runs
            score_line += f" | Needs: {runs_needed} to win"
            if runs_needed <= 0:
                break

        print(score_line)

        if batting_team == "Player":
            batter_num = get_player_move()
            bowler_num = get_computer_move()
            print(f"You Batted: {batter_num} | Computer Bowled: {bowler_num}")
        else:
            bowler_num = get_player_move()
            batter_num = get_computer_move()
            print(f"Computer Batted: {batter_num} | You Bowled: {bowler_num}")

        if batter_num == bowler_num:
            print("🚨 OUT! Both played the same number.")
            wickets_lost += 1
        else:
            current_runs += batter_num
            print(f"💰 {batting_team} scores {batter_num} runs!")

        balls_bowled += 1
        time.sleep(0.5)

        if target is not None and current_runs >= target:
            print(f"\n🎉 {batting_team} reached the target!")
            break

    print("\n" + "=" * 40)
    print(f"--- {batting_team.upper()} INNINGS ENDED ---")
    print(f"Final Score: {current_runs}/{wickets_lost} in {balls_bowled // 6}.{balls_bowled % 6} overs")
    print("=" * 40)
    return current_runs

# --- Result Logic ---

def game_result(score1, score2, target, batting_first, batting_second):
    """Determines and prints the final result of the game."""
    print("\n\n--- FINAL RESULT ---")

    if score2 >= target:
        print(f"🎉 WINNER: {batting_second.upper()}!")
        print(f"{batting_second} wins by scoring {score2} (Target: {target})")
    elif score2 < target - 1:
        print(f"🏆 WINNER: {batting_first.upper()}!")
        print(f"{batting_first} wins by {target - 1 - score2} runs.")
    else:
        print("🤝 It's a Tie!")

# --- Main Game Function ---

def main():
    """Runs the full Hand Cricket game."""
    print("🏏 Welcome to Python Hand Cricket!")

    wickets, overs = get_game_settings()
    print(f"\nMatch set: {wickets} wickets, {overs} overs.")

    toss_winner, first_choice = toss()

    if first_choice == 'bat':
        batting_first = toss_winner
    else:
        batting_first = 'Computer' if toss_winner == 'Player' else 'Player'

    batting_second = 'Computer' if batting_first == 'Player' else 'Player'

    print("\n--- Match Summary ---")
    print(f"1st Innings: {batting_first} bats first")

    # 1st Innings
    score1 = run_innings(batting_first, batting_second, wickets, overs)
    target = score1 + 1

    print(f"\nTarget for {batting_second}: {target} runs")
    print(f"\n2nd Innings: {batting_second} bats")

    # 2nd Innings
    score2 = run_innings(batting_second, batting_first, wickets, overs, target)

    game_result(score1, score2, target, batting_first, batting_second)

    # 👇 Added for Arcade Return
    input("\nPress Enter to return to the Arcade Menu...")

# --- Entry Point ---
if __name__ == "__main__":
    main()
