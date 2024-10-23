#Play Rock Paper Scissors against computer

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 0 and choice <= 2:
  print(images[choice])
else:
  print("That's not an option. You lose.")
  exit()

print("\nComputer chooses:")
computer = random.randint(0, 2)
print(images[computer])

if choice == computer:
  print("It's a tie!")
elif (choice < 2 and computer == choice + 1) or (choice == 2 and computer == 0):
  print ("You lose!")
else:
  print ("You win!")
exit()
