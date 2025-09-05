import random

print("Hello, welcome to my guessing game! The range will be 1-50, and you will only have 7 chances :D \nGood luck!!!")

answer = random.randint(1, 50)
guesses = 0
chances = 7
win = 0

while guesses < chances:
    guesses += 1
    guess = int(input("\nGuess a number between 1 and 50: "))
    if guess == answer:
        win = True
        break
    elif guess < answer:
        print("Sorry, you guessed the number too low!")
    elif guess > answer:
        print("Sorry, you guessed the number too high!")

if win == 1:
    print(f"Congratulations! You guessed the number correctly in only {guesses} tries!")
elif win == 0:
    print(f"The number was {answer}, Better luck next time!")