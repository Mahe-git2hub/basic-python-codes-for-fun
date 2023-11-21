import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 22.")

    # Generate a random number between 1 and 22
    secret_number = random.randint(1, 22)
    guesses_left = 5

    while guesses_left > 0:
        print(f"You have {guesses_left} guesses left.")

        # Get the user's guess
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the right number!")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        guesses_left -= 1

    if guesses_left == 0:
        print(f"Sorry, you're out of guesses. The number was {secret_number}.")

    print("Game Over. Thanks for playing!")

# Start the game
guess_the_number()
