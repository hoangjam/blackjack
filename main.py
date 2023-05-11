############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
# import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(cards):
    card = ""
    index = random.randint(0, len(cards) - 1)
    card = cards[index]
    return card


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []
user_cards = []
computer_cards = []

#Deal cards to players
for i in range(0, 2):
    user_cards.append(deal_card(cards))
    computer_cards.append(deal_card(cards))


def calculate_score(cards_list):
    total = sum(cards_list)
    if len(cards_list) == 2:
        if total == 21:

            # blackjack
            return 0
    for c in cards_list:
        # for Aces (11) to turn into 1
        if c == 11 and total > 21:
            cards_list.remove(c)
            cards_list.append(1)

            return sum(cards_list)
        elif total > 21:

            return sum(cards_list)

    return sum(cards_list)


def compare(user_score, computer_score):
    if user_score == 21:
        print(f"Player total: {user_score}")
        print("----------")
        print("PLAYER WIN\n")
    # elif user_score > 21:
    #     print(f"Player total: {user_score}")
    #     print("----------")
    #     print("BUST\n")

    # elif user_score == 0:
    #     print("----------")
    #     print("PLAYER BLACKJACK\n")

    # elif computer_score == 0:
    #     print("----------")
    #     print("DEALER BLACKJACK\n")

    # dealer draws to 18, stands on 17
    elif user_score == computer_score and computer_score > 18:
        print(f"Dealer total: {computer_score}")
        print("----------")
        print(f"Player total: {user_score}")
        print("----------")
        print("PUSH\n")
    else:
        print(f"Dealer total: {computer_score}")
        print("----------")
        print(f"Player total: {user_score}\n")


def game():
    keep_playing = True
    print(logo)
    while keep_playing:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nDealer total: {computer_score}")
        print("----------")
        print(f"Player total: {user_score}\n")

        if user_score == 0:
            print("----------")
            print("PLAYER BLACKJACK\n")
            keep_playing = False
            new_game()
        elif computer_score == 0:
            print("----------")
            print("DEALER BLACKJACK\n")
            keep_playing = False
            new_game()
        elif user_score > 21:
            print(f"Player total: {user_score}")
            print("----------")
            print("BUST\n")
            keep_playing = False
            new_game()
        else:
            check = input("Would you like another card? y/n: ")

        if check == "y":
            user_cards.append(deal_card(cards))
        else:
            keep_playing = False


def new_game():
    new_game = input("Would you like to start a new game? y/n: ")
    if new_game == "y":
        # need to clear console and objects here
        game()
    else:
        return "Bye"


game()

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
