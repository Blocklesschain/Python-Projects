import random 
from time import sleep

userScore = 0
computerScore = 0

userName = input(f'Enter your name to start game: ')

def userInput():
    return input()

def display (data):
    print(data)

def computerChoice():
    return random.choice(['rock', 'paper', 'scissors'])

def decision(computerSelection, userSelection):
    global userScore, computerScore
    if computerSelection == userSelection:
        sleep(1)
        display(f'{userName} selected {userSelection} and computer selected {computerSelection}')
        sleep(1)
        display('Round ended in a draw')
        showResult()
    elif userSelection == 'rock':
        if computerSelection == 'scissors':
            sleep(1)
            display(f'{userName} won this round')
            userScore += 1
            showResult()
        else: 
            sleep(1)
            display('computer won this round')
            computerScore += 1
            showResult()
    elif userSelection == 'scissors':
        if computerSelection == 'paper':
            sleep(1)
            display(f'{userName} won this round')
            userScore += 1
            showResult()
        else:
            sleep(1)
            display('computer won this round')
            computerScore += 1
            showResult()
    elif userSelection == 'paper':
        if computerSelection == 'rock':
            sleep(1)
            display(f'{userName} won this round')
            userScore += 1
            showResult()
        else:
            sleep(1)
            display('computer won this round')
            computerScore += 1
            showResult()
    else:
        sleep(1)
        display('invalid input')

def again():
    display('\nEnter 1. to play again or 2. to quit')
    user = userInput()
    if user == '1':
        sleep(1)
        game()
    elif user == '2':
        sleep(1)
        display('Thanks for playing the game. Final scores:')
        showResult()
        quit()
    else:
        sleep(1)
        display('\nInvalid Entry... try again')
        again()

def showResult():
    sleep(1)
    display(f'{userName} score: {userScore} computer score: {computerScore}')
    again()

def game():
    comp = computerChoice()
    display('\nComputer has made a selection')
    sleep(1)
    display('Enter rock or paper or scissors: ')
    user = userInput().lower()
    decision(comp, user)
    again()

def welcome():
    display(f'Hi {userName}, Welcome to python rock paper scissors game')
    game()

welcome()


#This code is not AI generated, rather written and maintained by Proffgodswill
#You can contact me on github @Blocklesschain
#or on twitter @Proffgodswill
#or on email proffgodswill@gmail.com