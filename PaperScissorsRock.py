#Write a program that allows users to play rock, paper, scissors against the computer. The program should:
#1. Prompt the user to enter their choice (rock, paper, or scissors).
#2. Generate a random choice for the computer.
#3. Compare the user's choice with the computer's choice to determine the winner.

import random
def play_RockPaperScissors():
    choices = ['rock', 'paper', 'scissors']
    userChoice = input("Make a choice: rock, paper, or scissors: ").lower()
    
    if userChoice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return
    
    computerChoice = random.choice(choices)
    print(f"Computer chose: {computerChoice}")
    
    if userChoice == computerChoice:
        print("It's a tie!")
    elif (userChoice == 'rock' and computerChoice == 'scissors') or \
         (userChoice == 'paper' and computerChoice == 'rock') or \
         (userChoice == 'scissors' and computerChoice == 'paper'):
        print("You win!")
    else:
        print("You lose!")
play_RockPaperScissors()