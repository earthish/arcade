import random
import time

# --- Helper Functions ---

def draw_card():
    """Draws a random card and returns its value."""
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card = random.choice(cards)
    
    # Convert face cards to value
    if card in ['J', 'Q', 'K']:
        value = 10
    elif card == 'A':
        value = 11  # initially 11, can later adjust
    else:
        value = int(card)
    
    return card, value

def calculate_total(hand):
    """Calculates total score for a hand and handles Aces."""
    total = sum(value for _, value in hand)
    # Adjust Ace(s) from 11 to 1 if total exceeds 21
    for card, value in hand:
        if total > 21 and card == 'A':
            total -= 10
    return total

def display_hand(name, hand, hide_first=False):
    """Displays the player's or dealer's hand."""
    if hide_first:
        print(f"{name}'s Hand: [?, {hand[1][0]}]")
    else:
        cards = [card for card, _ in hand]
        total = calculate_total(hand)
        print(f"{name}'s Hand: {cards}  | Total: {total}")

# --- Main Blackjack Function ---

def play_blackjack():
    print("\n🃏 Welcome to Mini Blackjack! 🃏")
    time.sleep(0.5)

    # Initial hands
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    # Show hands (dealer hides one card)
    display_hand("Dealer", dealer_hand, hide_first=True)
    display_hand("Player", player_hand)

    # --- Player's Turn ---
    while True:
        total = calculate_total(player_hand)
        if total > 21:
            print("💥 You busted! Dealer wins.")
            return

        choice = input("Do you want to 'hit' or 'stand'? ").strip().lower()
        if choice in ['hit', 'h']:
            new_card = draw_card()
            player_hand.append(new_card)
            print(f"You drew: {new_card[0]}")
            display_hand("Player", player_hand)
        elif choice in ['stand', 's']:
            break
        else:
            print("Invalid input. Type 'hit' or 'stand'.")

    # --- Dealer's Turn ---
    print("\nDealer's Turn:")
    time.sleep(0.5)
    display_hand("Dealer", dealer_hand)

    while calculate_total(dealer_hand) < 17:
        new_card = draw_card()
        dealer_hand.append(new_card)
        print(f"Dealer draws: {new_card[0]}")
        time.sleep(0.5)
        display_hand("Dealer", dealer_hand)

    # --- Results ---
    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)

    print("\n🎯 Final Results:")
    display_hand("Player", player_hand)
    display_hand("Dealer", dealer_hand)

    if dealer_total > 21:
        print("🏆 Dealer busted! You win!")
    elif player_total > dealer_total:
        print("🏆 You win!")
    elif player_total < dealer_total:
        print("💻 Dealer wins!")
    else:
        print("🤝 It's a tie!")

# --- Run the Game ---
if __name__ == "__main__":
    play_blackjack()
