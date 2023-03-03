# Imports
import random
import art

# Function to calculate score and check for blackjack
def calculate_score(list_of_cards):
    # Check ace + face card
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
    
    # Check if hand has ace and over 21 and change ace value
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)

    # Return res otherwise
    return sum(list_of_cards)

# Function to return a random card from the deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Function to compare scores at end of game
def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "You and the dealer have the same score. It's a draw."
    elif dealer_score == 0:
        return "Dealer has Blackjack, you lose."
    elif user_score == 0:
        return "You have 21. You win."
    elif user_score > 21:
        return "You went over 21. You lose"
    elif dealer_score > 21:
        return "Dealer busted. You win."
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "You lose."


# Start game
def play():

    # Print logo
    print(art.logo)

    # User and dealer's hands
    user_hand = []
    dealer_hand = []

    # Bool to keep track of game state
    is_game_over = False

    # Deal cards
    for _ in range (2):
        user_hand.append(deal_card())
        dealer_hand.append(deal_card())

    # Start user's turn
    while not is_game_over:
            
        # Calculate scores of the players
        user_score = calculate_score(user_hand)
        dealer_score = calculate_score(dealer_hand)

        # Print user cards and computer's first card
        print(f"Your cards: {user_hand}. Current score: {user_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        # Print results or continue turn
        if user_score == 0 and dealer_score == 0:
            print("You and the dealer both have Blackjack. Push.")
            is_game_over = True
        elif user_score > 21:
            print("You went over 21. You lose.")
            is_game_over = True
        else:
            another_card = input("Do you want to draw another card? Type 'y' or 'n'. ")
            if another_card == 'y':
                user_hand.append(deal_card())
                user_score = calculate_score(user_hand)
            else:
                is_game_over = True

    # Dealer's turn            
    while dealer_score != 0 and dealer_score <= 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    # End of game results
    print(f"Your final hand: {user_hand}. Final score: {user_score}")
    print(f"Dealer's final hand: {dealer_hand}. Dealer final score: {dealer_score}")
    print(compare(user_score, dealer_score))

# Replay option
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play()

