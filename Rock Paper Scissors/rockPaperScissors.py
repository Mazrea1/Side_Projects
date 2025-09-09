import random

#print the rules and game tally

print("Welcome to Rock, Paper, Scissors! \n"
      "The rules are simple: \n"
      "Rock beats Scissors \n"
      "Scissors beats Paper \n"
      "Paper beats Rock \n"
      "You will be playing against the computer. \n"
      "The Score will be posted at the end! \n"
      "Good luck!!!")

playerWins = 0
computerWins = 0
ties = 0
totalGames = 0

#Main Game Loop
while True:
    choice = int(input(" Choose rock, paper, or scissors! \n"
                       "1. Rock, 2. Paper, 3. Scissors \n"))
    computerChoice = random.randint(1, 3)

    #Game Logic
    if choice == 1 and computerChoice == 1:
        print("You chose Rock, Computer chose Rock! It's a tie!")
        ties += 1
        endGame = input("\nDo you want to play again? (y/n)")
        if endGame == "n":
            break
    if choice == 1 and computerChoice == 2:
        print("You chose Rock, Computer chose Paper! You lose!")
        computerWins += 1
        endGame = input("\nDo you want to play again? (y/n)")
        if endGame == "n":
            break
    if choice == 1 and computerChoice == 3:
        print("You chose Rock, Computer chose Scissors! You win!")
        playerWins += 1
        endGame = input("\nDo you want to play again? (y/n)")
        if endGame == "n":
            break
    if choice == 2 and computerChoice == 1:
        print("You chose Paper, Computer chose Rock! You win!")
        playerWins += 1
        endGame = input("\nDo you want to play again? (y/n)")
        if endGame == "n":
            break
    if choice == 2 and computerChoice == 2:
        print("You chose Paper, Computer chose Paper! It's a tie!")
        ties += 1
        endGame = input("\nDo you want to play again? (y/n)")
        if endGame == "n":
            break
    if choice == 2 and computerChoice == 3:
        print("You chose Paper, Computer chose Scissors! You lose!")
        computerWins += 1
        endGame = input("\nDo you want to play again? (y/n)")
        if endGame == "n":
            break
    if choice == 3 and computerChoice == 1:
        print("You chose Scissors, Computer chose Rock! You lose!")
        computerWins += 1
        endGame = input("\nDo you want to play again? (y/n)")
        if endGame == "n":
            break
    if choice == 3 and computerChoice == 2:
        print("You chose Scissors, Computer chose Paper! You win!")
        playerWins += 1
        endGame = input("\nDo you want to play again? (y/n)")
        if endGame == "n":
            break
    if choice == 3 and computerChoice == 3:
        print("You chose Scissors, Computer chose Scissors! It's a tie!")
        ties += 1
        endGame = input("\nDo you want to play again? (y/n)")
        if endGame == "n":
            break

    else:
        print("That wasn't one of the choices, try again!")


#End of Game and Score
totalGames  = playerWins + computerWins + ties
print("That was fun! Here's the score: \n"
      f"You won {playerWins} times! \n"
      f"The computer won {computerWins} times! \n"
      f"You tied {ties} times! \n"
      f"You played a total of {totalGames} games! \n")