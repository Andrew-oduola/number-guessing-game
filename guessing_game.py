# Guessing Game with Python
# Code With DreX

import random

def get_user_input(promt):
    return input(promt).strip()

def play_round():
    tries_left = 3
    secret_number = random.randint(1, 5)

    print("Let's Play the guessing game! You have 3 chances to guess the right number between 1 and 5.")

    while tries_left > 0:
        try: 
            guess = int(get_user_input('Your guess: '))
        except ValueError:
            print('Please enter a valid number')
            continue

        if guess == secret_number:
            print('You won!')
            return 1  # point for winning the game (score)
        else: 
            print('Try again')

        tries_left -= 1 

    print('Game Over')
    return 0 

def main():
    score = 0
    
    while True:
        answer = get_user_input("Do you want to continue playing (Y/N)? ").lower()

        if answer == 'y':
            score += play_round()
            print(f"Current Score: {score}")
        elif answer == 'n':
            print(f"Final Score: {score}")
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'. ")

main()