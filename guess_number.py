# Number guessing game

secret_number = 7
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Correct! You guessed it.")
else:
    print("Wrong guess. Try again.")
