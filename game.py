# Imports
import random

# List of cards for game :)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function to run game
def play():

    # User and dealer's hands
    user_hand = []
    dealer_hand = []

    # Prompt user
    ans = input(print("Do you want to play Blackjack? Type 'y' or 'n': "))

    # Start user's turn
    while ans == 'y':
        # Give user cards
        for i in range(2):
            user_hand.append(int(random.choice(cards)))
        
        # Give dealer a card
        dealer_hand.append(int(random.choice(cards)))

        # Calculate score
        user_score = sum(user_hand)

        # Print results for user to continue
        print(f"Your cards: are {user_hand}. Your score is {user_score}")
        print(f"Computer's first card: {dealer_hand[0]}")

        another_card(user_score, user_hand)
        ans = 'n'
        # # User's turn
        # turn_over = False # Bool to hold turn status
        # while turn_over == False: 
        #     # Prompt user
        #     cont = input("Type 'y' to get another card, or 'n' to pass ")
        #     # If yes
        #     if cont == 'y':
        #         # Give card
        #         user_hand.append(int(random.choice(cards)))

        #         # Calculate results
        #         user_score = sum(user_hand)

        #         # Check user's hand validity
        #         if user_hand > 21:
        #             print(f"Your final hand: {user_hand}. Final score {user_score}")
        #         else:

def another_card(score, hand):
    # User's turn
    turn_over = False # Bool to hold turn status

    while turn_over == False: 
        # Prompt user
        cont = input("Type 'y' to get another card, or 'n' to pass ")
        # If yes
        if cont == 'y':
            # Give card
            hand.append(int(random.choice(cards)))
        else:
            turn_over = True

        # Calculate results
        score = sum(hand)

        # Check user's hand validity
        if score > 21:
            print(f"Your final hand: {hand}. Final score: {score}.")
            print("You went over 21. You lose.")
            turn_over = True
        else:
            print(f"Your cards: are {hand}. Your score is {score}")
            another_card(score, hand)



# Run game
play()