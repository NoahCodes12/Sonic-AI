import random

def create_deck():
    """
    Create a standard 52-card deck, shuffle it, and return the shuffled deck.
    Each card is represented as a tuple containing its rank and suit.
    """
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    """
    Calculate the total value of the cards in a hand.
    Aces can count as 11 or 1 to avoid busting.
    """
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
    
    # Adjust for aces, changing them from 11 to 1 if necessary to avoid busting.
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def is_blackjack(hand):
    """
    Check if the hand has a blackjack (a value of exactly 21).
    """
    return calculate_hand_value(hand) == 21

def is_bust(hand):
    """
    Determine if the hand is bust (exceeds a value of 21).
    """
    return calculate_hand_value(hand) > 21

def deal_card(deck):
    """
    Remove a card from the top of the deck and return it.
    """
    return deck.pop()

def display_hand(hand, player_name):
    """
    Display the hand for the specified player, including the card representation and hand value.
    """
    hand_str = ' '.join([f"{rank}{suit}" for rank, suit in hand])
    print(f"{player_name}'s hand: {hand_str}, value: {calculate_hand_value(hand)}")

def player_turn(deck, player_hand):
    """
    Conduct the player's turn, allowing them to hit or stand.
    The turn ends if the player stands, busts, or gets blackjack.
    """
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
    """
    Play out the dealer's turn by drawing cards until the hand value is at least 17.
    """
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
    display_hand(dealer_hand, "Dealer")
    if is_bust(dealer_hand):
        print("Dealer busts! Player wins.")
        return False
    return True

def determine_winner(player_hand, dealer_hand, bet, player_balance):
    """
    Compare the values of the player's and dealer's hands to determine the winner.
    Update player's balance based on the outcome of the round.
    """
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    if player_value > 21:  # Player busts
        print("Player busts! Dealer wins.")
        player_balance -= bet
    elif dealer_value > 21:  # Dealer busts
        print("Dealer busts! Player wins!")
        player_balance += bet
    elif player_value > dealer_value:  # Player wins by having higher value
        print("Player wins!")
        player_balance += bet
    elif player_value < dealer_value:  # Dealer wins by having higher value
        print("Dealer wins!")
        player_balance -= bet
    else:  # Tie
        print("It's a tie!")

    return player_balance

def play_blackjack():
    """
    Set up and manage a complete game of Blackjack.
    Players are given the option to play multiple rounds until they decide to stop.
    """
    player_balance = int(input("Enter your initial balance: "))  # Input initial balance
    min_bet = 10

    while player_balance >= min_bet:
        print(f"\nPlayer Balance: {player_balance}")
        bet = int(input(f"Place your bet (minimum bet is {min_bet}): "))
        if bet < min_bet or bet > player_balance:
            print("Invalid bet amount. Please place a bet within your balance.")
            continue

        deck = create_deck()  # Create and shuffle a new deck for each game
        
        player_hand = [deal_card(deck), deal_card(deck)]  # Deal initial two cards to the player
        dealer_hand = [deal_card(deck), deal_card(deck)]  # Deal initial two cards to the dealer
        
        print("\nWelcome to Blackjack!")
        display_hand(dealer_hand[1:], "Dealer")  # Show dealer's hand with one card down
        display_hand(player_hand, "Player")  # Show player's hand
        
        if is_blackjack(player_hand):  # Check for player's blackjack
            print("Player has blackjack! Player wins!")
            player_balance += int(bet * 1.5)
        else:
            if player_turn(deck, player_hand):  # If player doesn't bust, dealer takes their turn
                if dealer_turn(deck, dealer_hand):
                    player_balance = determine_winner(player_hand, dealer_hand, bet, player_balance)  # Determine the outcome of the round
                else:
                    player_balance += bet  # Dealer busts, player wins
            else:
                player_balance -= bet  # Player busts, dealer wins
        
        print(f"\nNew Player Balance: {player_balance}")
        
        if player_balance < min_bet:
            print("\nInsufficient balance. Game over!")
            break
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()  # Ask player if they want to play another round
        if play_again != 'yes':
            print("Thank you for playing!")
            break  # Exit the game loop if the player doesn't want to play again

# Start the game
play_blackjack()
