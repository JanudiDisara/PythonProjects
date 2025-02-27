import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
correct_number = random.randint(1, 100)
attempts = 0
over = False

if level == 'easy':
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
elif level == 'hard':
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")

def guess_number():
    number = int(input("Make a guess: "))
    return number

def check_number(guessed_number, actual_number, no_of_attempts):
    global over
    if guessed_number == actual_number:
        print(f"You got it! The answer was {actual_number}")
        over = True
    else:
        no_of_attempts -= 1
        if guessed_number > actual_number and no_of_attempts != 0:
            print(f"Too high.\nGuess again.\nYou have {no_of_attempts} attempts remaining to guess the number.")
        elif guessed_number < actual_number and no_of_attempts != 0:
            print(f"Too low.\nGuess again.\nYou have {no_of_attempts} attempts remaining to guess the number.")

while attempts != 0:
    if over is True:
        break
    else:
        check_number(guess_number(), correct_number, attempts)
        attempts -= 1

if attempts == 0:
    print("You've run out of guesses. Refresh the page to run again.")