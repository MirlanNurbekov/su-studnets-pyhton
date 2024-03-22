import random

def get_validated_input(prompt, min_val, max_val):
    """Prompt the user for input and validate it."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def select_difficulty():
    """Let the user select a difficulty level and return the corresponding attempts limit and range."""
    print("Select a difficulty level:")
    print("1: Easy (1-100, 10 attempts)")
    print("2: Medium (1-200, 7 attempts)")
    print("3: Hard (1-300, 5 attempts)")
    difficulty = get_validated_input("Choose a difficulty (1, 2, 3): ", 1, 3)
    
    if difficulty == 1:
        return 10, 100
    elif difficulty == 2:
        return 7, 200
    else:
        return 5, 300

def guess_the_number():
    print("Welcome to the Enhanced Guess the Number Game!")
    
    attempts_limit, max_number = select_difficulty()
    secret_number = random.randint(1, max_number)
    
    print(f"I'm thinking of a number between 1 and {max_number}.")

    attempts = 0
    while attempts < attempts_limit:
        guess = get_validated_input("Make a guess: ", 1, max_number)
        attempts += 1
        
        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    
    if attempts == attempts_limit and guess != secret_number:
        print(f"Sorry, you've used all your attempts. The number was {secret_number}.")

guess_the_number()
