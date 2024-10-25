import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
computer_cards = []

def score(card_list):
    if 11 in card_list and sum(card_list) > 21:
        card_list[card_list.index(11)] = 1
    return sum(card_list)

def compare(u_cards, c_cards):
    is_game_over = False
    if score(your_cards) == 21 and len(your_cards) == 2:
        print("  YOU WIN WITH BLACKJACK!!  ")
        is_game_over = True
    elif score(computer_cards) == 21 and len(computer_cards) == 2:
        print("  COMPUTER WINS WITH BLACKJACK :((  ")
        is_game_over = True
    elif not continue_drawing:
        if score(your_cards) > 21:
            print("  YOU WENT OVER. YOU LOSE :(")
        elif score(computer_cards) > 21:
            print("  COMPUTER WENT OVER. YOU WIN!!!")
        elif score(your_cards) == score(computer_cards):
            print("  IT'S A TIE.  ")
        elif score(your_cards) > score(computer_cards):
            print("  YOU WIN!!!  ")
        else:
            print("  YOU LOSE :(  ")

    return is_game_over

game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while game != 'y' and game != 'n':
    game = input("Please type 'y' for yes and 'n' for no: ").lower()
if game == 'n':
    print("Goodbye!")
    exit()
continue_playing = True
while continue_playing:
    continue_drawing = True
    print(logo)
    for _ in range(2):
        your_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    print(f"Your cards: {your_cards}, current score: {score(your_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    game_over = compare(your_cards, computer_cards)
    if not game_over:
        while continue_drawing:
            continue_drawing = True
            draw_more = input("Type 'y' to get another card, type 'n' to pass: ")
            while draw_more != 'y' and draw_more != 'n':
                draw_more= input("Please type 'y' for yes and 'n' for no: ").lower()
            if draw_more == 'n':
                continue_drawing = False
            else:
                your_cards.append(random.choice(cards))
                print(f"Your cards: {your_cards}, current score: {score(your_cards)}")
                if score(your_cards) >= 21:
                    continue_drawing = False
                else:
                    print(f"Computer's first card: {computer_cards[0]}")
                    continue_drawing = True
        while score(your_cards) <= 21 and score(computer_cards) < 17:
            computer_cards.append(random.choice(cards))
        compare(your_cards, computer_cards)
    print(f"Your final hand: {your_cards}, final score: {score(your_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {score(computer_cards)}")
    new_game = input("Do you want to play again? Type 'y' or 'n': ")
    while game != 'y' and game != 'n':
        game = input("Please type 'y' for yes and 'n' for no: ").lower()
    if game == 'n':
        print("Goodbye!")
        continue_playing = False
    else:
        continue_playing = True
        your_cards = []
        computer_cards = []
        print("\n" * 80)

