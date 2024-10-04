import random
def guess_the_number():
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"Guess the number between {lower_bound} and {upper_bound}!")

    while True:
            guess = int(input(f"Guess the number: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")

guess_the_number()