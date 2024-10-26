import art
import game_data
import random

def intro(choice):
    """returns introduction sentence of the account"""
    sentence = f"{choice['name']}, {choice['description']} from {choice['country']}"
    return sentence

def check_correct(a_, b_):
    """returns a or b depending on who has more followers"""
    if a_['follower_count'] > b_['follower_count']:
        return "a"
    else:
        return "b"

def play_game():
    points = 0
    continue_game = True
    a = random.choice(game_data.data)
    while continue_game:
        b = random.choice(game_data.data)
        while a == b:
            b = random.choice(game_data.data)
        print(f"Compare A: {intro(a)}")
        print(art.vs)
        print(f"Against B: {intro(b)}")
        answer = input("\nWho has more followers? Type 'A' or 'B': ").lower()
        while answer not in ["a", "b"]:
            answer = input("Please type 'A' or 'B': ").lower()
        correct = check_correct(a, b)
        print("\n" * 40)
        print(art.logo)
        if answer == correct:
            continue_game = True
            points += 1
            print(f"You're right! Current score: {points}")
            a = b
        else:
            continue_game = False
            return points

print(art.logo)
score = play_game()
print(f"Sorry, that's wrong. Final score: {score}")
