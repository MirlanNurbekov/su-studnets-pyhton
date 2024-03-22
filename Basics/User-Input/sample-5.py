import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Randomly select a number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts_limit = 7
    attempts = 0
    
    while attempts < attempts_limit:
        guess = int(input("Make a guess: "))
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