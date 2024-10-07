import random

def play_game():
    # generate a random number between 1 and 50
    secret_number = random.randint(1, 50)

    while True:
        # prompt the user to guess the number
        guess = int(input("Guess the number between 1 and 50: "))

        # compare the guess to the secret number
        if guess < secret_number:
            print("Too low, try again.")
        elif guess > secret_number:
            print("Too high, try again.")
        else:
            print("Congratulations!")
            break   # exit the loop when the guess is correct

    print()  # add a blank line for readability

# play the game repeatedly until the user chooses to quit
while True:
    play_game()
    answer = input("Do you want to play again? (y/n) ").lower()
    if answer != 'y':
        break
