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

    # Start game
    while ans == 'y':
        # Give user cards
        for i in range(2):
            user_hand.append(int(random.choice(cards)))
        
        # Give dealer a card
        dealer_hand.append(int(random.choice(cards)))

        # Calculate score
        user_score = 0
        for card in range(len(user_hand)):
            user_score += user_hand[card]

        # Print results for user to continue
        print(f"Your cards: are {user_hand}. Your score is {user_score}")
        print(f"Computer's first card: {dealer_hand[0]}")

        # User's turn
        turn_over = False # Bool to hold turn status
        while turn_over == False: 
            # Prompt user
            cont = input("Type 'y' to get another card, or 'n' to pass")
            # If yes
            if cont == 'y':
                user_hand.append(int(random.choice(cards))) # Give card

                # Calculate results
                user_score = 0
                for card in range(len(user_hand)):
                    user_score += card

                # Check user's hand validity
                if user_hand > 21:
                    print("Your score is over 21. You lose")

                
                #print(f"Your cards: are {user_hand}. Your score is {user_score}") # Print results




# Run game
play()