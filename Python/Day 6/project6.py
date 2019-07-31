import random

TRY = 10

print("Welcome to the number guessing game! Guess the number from 1-20. You have 10 attempts.")

def loop():
    restart = input("Do you wish to start again? type \"yes\" to restart: ")
    if restart == "yes":
        game()
    else:
        print("Thanks for playing! Game made by @tohkyr")
        exit()

def game():
    number = random.randint(1, 20)
    attempts = 0
    while attempts < TRY:
        try:
            guess = int(input("Enter Number here from 1-20: "))
        except ValueError:
            print("That's not a number, try again.")
            continue

        attempts += 1

        if guess > 20 or guess < 1:
            print("Out of range!")
            attempts -= 1

        else:
            if guess < number:
                print("Go higher.")
            elif guess > number:
                print("Go lower.")
            else:
                print("You won! The number was " + str(number) + "!")
                print("Your attempts: " + str(attempts))
                loop()

            if attempts == TRY:
                print("Game over! You ran out of attempts!")
                print("The number was " + str(number))
                loop()

game()
