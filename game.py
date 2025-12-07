import random
print('--- Welcome to the Number Guessing Game ---')
while True:
    secret_number = random.randint(1, 20)
    attempts = 6
    while attempts > 0:
        guess = input('Guess the number (1-20) or q to quit: ')
        if guess.lower() == "q":
            print("Exiting game... Goodbye!")
            exit()
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input! Please enter a number or 'q'.")
            continue
        if guess > secret_number:
            print('Too high!')
            attempts -= 1
        elif guess < secret_number:
            print('Too low!')
            attempts -= 1
        else:
            print(f'Congratulations! You guessed it in {6 - attempts + 1} attempts.')
            break
        if attempts > 0:
            print(f"Attempts left: {attempts}")
        else:
            print(f'You lost the game! The secret number was {secret_number}')
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thanks for playing! Goodbye!")
        break