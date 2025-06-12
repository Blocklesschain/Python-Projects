#Write a program to play the game hangman. The program should:
#1. Choose a random word from a predefined list of words.
#2. Allow the user to guess letters in the word.
import random

def play_Hangman():
    words = ['python', 'hangman', 'programming', 'computer', 'science']
    word_to_guess = random.choice(words)
    guessed_letters = set()
    attempts = 25
    word_completion = '_' * len(word_to_guess)

    print("Welcome to Hangman!")
    
    while attempts > 0 and '_' in word_completion:
        print(f"\nWord: {word_completion}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)

        if guess in word_to_guess:
            word_completion = ''.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

    if '_' not in word_completion:
        print(f"Congratulations! You guessed the word: {word_to_guess}")
    else:
        print(f"Game over! The word was: {word_to_guess}")
play_Hangman()