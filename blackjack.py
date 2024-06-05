import random

def create_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for rank, suit in hand:
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            num_aces += 1
            value += 11
        else:
            value += int(rank)
    
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    
    return value

def is_blackjack(hand):
    return calculate_hand_value(hand) == 21

def is_bust(hand):
    return calculate_hand_value(hand) > 21

def deal_card(deck):
    return deck.pop()

def display_hand(hand, player_name):
    hand_str = ' '.join([f"{rank}{suit}" for rank, suit in hand])
    print(f"{player_name}'s hand: {hand_str}, value: {calculate_hand_value(hand)}")

def player_turn(deck, player_hand):
    while True:
        display_hand(player_hand, "Player")
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.append(deal_card(deck))
            if is_bust(player_hand):
                display_hand(player_hand, "Player")
                print("Player busts! Dealer wins.")
                return False
        elif action == 'stand':
            break
        else:
            print("Invalid action. Please choose 'hit' or 'stand'.")
    return True

def dealer_turn(deck, dealer_hand):
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
    display_hand(dealer_hand, "Dealer")
    if is_bust(dealer_hand):
        print("Dealer busts! Player wins.")
        return False
    return True

def determine_winner(player_hand, dealer_hand):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    if player_value > dealer_value:
        print("Player wins!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

def play_blackjack():
    while True:
        deck = create_deck()
        
        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]
        
        print("Welcome to Blackjack!")
        display_hand(dealer_hand, "Dealer")
        display_hand(player_hand, "Player")
        
        if is_blackjack(player_hand):
            print("Player has blackjack! Player wins!")
        else:
            if player_turn(deck, player_hand):
                if dealer_turn(deck, dealer_hand):
                    determine_winner(player_hand, dealer_hand)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

# Start the game
play_blackjack()


