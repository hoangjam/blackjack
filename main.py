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

import random
from replit import clear
from art import logo


def deal_card():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # card = ""
    # index = random.randint(0, len(cards) - 1)
    # card = cards[index]
    card = random.choice(cards)
    return card


def calculate_score(cards_list):
    total = sum(cards_list)

    if len(cards_list) == 2 and total == 21:
        return 0

    if 11 in cards_list and total > 21:
        cards_list.remove(11)
        cards_list.append(1)

    return total


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "PUSH\n"
    elif computer_score == 0:
        return "DEALER HAS BLACKJACK\n"
    elif user_score == 0:
        return "PLAYER HAS BLACKJACK\n"
    elif user_score > 21:
        return "BUST\n"
    elif computer_score > 21:
        return "DEALER BUST\n"
    elif user_score > computer_score:
        return "PLAYER WINS\n"
    else:
        return "DEALER WINS\n"


def game():
    print(logo)

    user_cards = []
    computer_cards = []
    game_over = False
    """Deal cards to players"""
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print("********************\n")
        print(f"DEALER showing: {computer_cards[0]}\n")
        print("--------------------\n")
        print(f"PLAYER cards: {user_cards} Total: {user_score}\n")
        print("********************\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            another_card = input("Would you like another card? y/n: ")
            if another_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
    """Dealer receiving cards"""
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    clear()
    print("********************\n")
    print(f"DEALER showing: {computer_cards}, total: {computer_score}\n")
    print(f"PLAYER has: {user_cards}, total: {user_score}\n")
    print("********************\n")
    print(compare(user_score, computer_score))


game()

while input("Do you want to play more Blackjack? y/n: ") == "y":
    clear()
    game()

print("\nGood game, bye")
