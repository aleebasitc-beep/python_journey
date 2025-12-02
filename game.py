import random
print('---welcome! to the number guessing game---')
secret_number = random.randint(1, 20)
attempts = 6
while attempts > 0:
    guess = int(input('Guess the number (1, 20): '))
    if guess > secret_number:
        print('too high!')
        attempts -=1
    elif guess < secret_number:
        print('too low!')
        attempts -=1
    elif guess == secret_number:
        print('congratulations! you guessed it.')
    if attempts > 0 and guess != secret_number:
        print(f"attempts left: {attempts}")
    elif attempts ==0:
        print(f'You lost the game! the secret number was {secret_number}')