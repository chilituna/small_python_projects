import random

logo = r"""
  _,  ,  ,  _, _, _,    ___, ,  _,   ,  , ,  , , ,  __   _,,_   
 / _  |  | /_,(_,(_,   ' | |_|,/_,   |\ | |  ||\/| '|_) /_,|_)  
'\_|`'\__|'\_  _) _)     |'| |'\_    |'\|'\__|| `| _|_)'\_'| \  
  _|     `   `'  '       ' ' `   `   '  `    `'  `'       `'  `                                                              
"""

EASY = 10
HARD = 5

def set_difficulty():
    difficulty = input("Choose difficulty: type 'easy' or hard': ")
    if difficulty == "easy":
        return EASY
    else:
        return HARD

def check_if_correct(guessed, correct, count):
    if guessed == correct:
        print("That is correct!\n")
        return -1
    elif guessed < correct:
        print("Too low!")
    else:
        print("Too high!")
    return count - 1


start_over = True
while start_over:
    number = random.randint(1, 100)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    counter = set_difficulty()
    print(f"You have {counter} attempts to guess the number.")
    while counter > 0:
        while True:
            try:
                guess = int(input("Make a guess: "))
                break
            except:
                print("Invalid input. Please give a number.")
        counter = check_if_correct(guess, number, counter)
        if counter == -1:
            break
        if counter == 0:
            print(f"You have {counter} guesses left. The correct number would have been {number}.\n")
        else:
            print(f"Guess again. You have {counter} guesses left")
    play_again = input("Play again? type 'y' for yes and 'n' for no: ")
    while play_again not in ["y", "n"]:
        play_again = input("Please type 'y' or 'n': ")
    if play_again == "n":
        start_over = False
    else:
        print("\n" * 30)
print("Goodbye!")
