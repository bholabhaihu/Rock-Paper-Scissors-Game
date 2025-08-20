import random
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

# User Input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)

# Computer Input
print("Computer Choice")

computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if user_choice >= 3 or user_choice < 0:
    print("You lose")
elif user_choice == 0 and computer_choice == 0:
    print("Draw")
elif user_choice == 0 and computer_choice == 1:
    print("You Lose")
elif user_choice == 0 and computer_choice == 2:
    print("You Win")
elif user_choice == 1 and computer_choice == 0:
    print("You Win")
elif user_choice == 1 and computer_choice == 1:
    print("Draw")
elif user_choice == 1 and computer_choice == 2:
    print("You Lose")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose")
elif user_choice == 2 and computer_choice == 1:
    print("You Win")
elif user_choice == 2 and computer_choice == 2:
    print("Draw")
