import random
import os
import time


def hangman():
    word_list = ['python', 'hangman', 'game', 'openai', 'programming']
    word = random.choice(word_list)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            attempts -= 1
            print("Attempts remaining:", attempts)

        word_progress = ""
        for letter in word:
            if letter in guessed_letters:
                word_progress += letter + " "
            else:
                word_progress += "_ "

        print(word_progress)

        if "_" not in word_progress:
            print("Congratulations! You won!")
            time.sleep(3)
            choice = input('play again? (y/n)')
        if choice == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            hangman()
        elif choice == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('exiting...')
            time.sleep(3)
            os.sytem('python games.py')

    if attempts == 0:
        print("Sorry, you lost. The word was:", word)


hangman()
