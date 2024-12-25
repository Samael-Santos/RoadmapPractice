import random


def difStep():
    print("\nPlease select the difficulty level:\n"
        "1. Easy (4 chances)\n"
        "2. Medium (3 chances)\n"
        "3. Hard (2 chances)")

    choice = input("Enter your choice: ")
    match choice:
        case "1":
            return gameStep("Easy", 4)
        case "2":
            return gameStep("Medium", 3)
        case "3":
            return gameStep("Hard", 2)
        case _:
            print("\nInvalid choice!")
            return difStep()


def gameStep(dif, chances):

    print(f"\nGreat! You have selected the {dif} difficulty level. Let's start the game!")
    tries = 0
    secret = random.randint(1, 10)


    while True:
        guess = input(f"(You have {chances} chances) Enter your guess: ")
        guess = int(guess)
        tries += 1
        chances -= 1

        if guess == secret:
            print(f"\nCongratulations! You guessed the correct number in {tries} attempts!")
            return againStep()
        elif guess > secret:
            print(f"\nIncorrect! The number is less than {guess}.")
        elif guess < secret:
            print(f"\nIncorrect! The number is greater than {guess}.")
        if chances == 0:
            print(f"Sorry, no attempts remaining. The number was {secret}.")
            return againStep()

def againStep():
    againChoice = input("Wanna play again?(y/n)")
    match againChoice:
        case "y":
            return difStep()
        case "n":
            return print("Come again!")
        case _:
            print("\nInvalid choice!")
            return againStep()

print("\nWelcome to the Number Guessing Game!\n"
      "Im thinking of a number between 1 and 10.\n"
      "You have 5 chances to guess the correct number.")

difStep()