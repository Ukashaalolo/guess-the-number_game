import random
def guess_the_number():
    print("Welcome to Guess the Number!")
    while True:
        try:
            lower_bound = int(input("Enter the lower bound of the range: "))
            upper_bound = int(input("Enter the upper bound of the range: "))
            if upper_bound > lower_bound:
                break
            else:
                print("Upper bound must be greater than lower bound")
        except ValueError:
            print("Please enter valid numbers.")
    number_to_guess = random.randint(lower_bound, upper_bound)
    max_guesses = 5
    attempts = 0
    guess_history = []
    print(f"\nYou have {max_guesses} attempts to guess the number between {lower_bound} and {upper_bound}.")
    while attempts < max_guesses:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            guess_history.append(guess)
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            remaining_guesses = max_guesses - attempts
            print(f"You have {remaining_guesses} guesses left.")
            print(f"Your previous guesses: {guess_history}")
        except ValueError:
            print("Please enter a valid number")
    if attempts == max_guesses and guess != number_to_guess:
        print("\nSorry, you've run out of guesses!")
        print(f"The correct number was {number_to_guess}. Better luck next time!")

guess_the_number()