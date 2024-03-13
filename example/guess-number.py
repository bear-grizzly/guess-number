import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number:
            print("Your guess is too low. Try again.")
        elif guess > number:
            print("Your guess is too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

if __name__ == "__main__":
    guess_number()
