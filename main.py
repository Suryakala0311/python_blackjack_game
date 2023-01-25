import random
from art import logo

card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def winner(user_total, computer_total):
    if user_total < 21 and computer_total < 21:
        if user_total < computer_total:
            print(f"Computer won and the number is {computer_total}")
        else:
            print(f"You won and the number is {user_total}")
    elif user_total > 21 and computer_total < 21:
        print(f"Computer won and the number is {computer_total}")
    elif computer_total > 21 and user_total < 21:
        print(f"You won and the number is {user_total}")
    elif user_total == 21 and computer_total < 21:
        print(f"You won and the number is {user_total}")
    elif user_total == 21 and computer_total > 21:
        print(f"You won and the number is {user_total}")
    elif user_total > 21 and computer_total == 21:
        print(f"Computer won and the number is {computer_total}")
    elif user_total < 21 and computer_total == 21:
        print(f"Computer won and the number is {computer_total}")
    elif user_total == computer_total:
        print("Match draw.")

user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
print(logo)

card = []
computer_card = []
def deal_card():
    card_input = int(random.choice(card_list))
    card.append(card_input)
    computer_card1 = int(random.choice(card_list))
    computer_card.append(computer_card1)
    return card, computer_card

if user_input == 'y':
    for _ in range(2):
        deal_card()
    print(f"Your cards: {card}")
    print(f"Computer's first card: {computer_card[0]}")
    
    user_next_input = user_input = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_next_input == 'y':
        deal_card()
        print(f"Your final cards: {card}")
        print(f"Computer final card: {computer_card}")
    else:
        winner(sum(card), sum(computer_card))

    user_total = sum(card)
    computer_total = sum(computer_card)

    winner(user_total, computer_total)
elif user_input == 'n':
    print("End Game.")



