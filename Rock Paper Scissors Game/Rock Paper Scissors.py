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

option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor. "))
if option == 0:
    print(rock)
elif option == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose: ")
computer_option = [0, 1, 2]
print(random.choice(computer_option))
if computer_option == 0:
    print(rock)
elif computer_option == 1:
    print(paper)
else:
    print(scissors)
if (option == 0 and computer_option == 1) or (option == 1 and computer_option == 2)\
        or (option == 2 and computer_option == 0):
    print("You lose")
elif (option == computer_option):
    print("It is a draw!")
else:
    print("You win")
