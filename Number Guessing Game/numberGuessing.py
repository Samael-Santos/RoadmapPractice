import random

tries = 0
secret = random.randint(1, 10)

print("Welcome to the Number Guessing Game!"
      "Im thinking of a number between 1 and 10."
      "You have 5 chances to guess the correct number.")

print("\nPlease select the difficulty level:"
      "1. Easy (10 chances)"
      "2. Medium (5 chances)"
      "3. Hard (3 chances)")

choice = input("Enter your choice: ")
match choice:
    case "1":
        dif = "Easy"
        chances = 4
    case "2":
        dif = "Medium"
        chances = 3
    case "3":
        dif = "Hard"
        chances = 2
    case _:
        print("Invalid choice")

print(f"\nGreat! You have selected the {dif} difficulty level."
      "Let's start the game!")

while True:
    guess = input(f"You have {chances} chances. Enter your guess: ")
    guess = int(guess)
    tries += 1
    chances -= 1

    if guess == secret:
        print("\nCongratulations!"
              f"You guessed the correct number in {tries} attempts.")
        break
    elif guess > secret:
        print(f"\nIncorrect! The number is less than {guess}.")
    elif guess < secret:
        print(f"\nIncorrect! The number is greater than {guess}.")
    if chances == 0:
        print(f"Sorry, no attempts remaining. The number was {secret}.")
        break
