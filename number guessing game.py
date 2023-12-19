import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    guess = int(input("Guess the number between 1 and 100: "))
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
    else:
        print(f"Wrong guess. The correct number was {secret_number}.")

# Usage
number_guessing_game()
