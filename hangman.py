import os
from random import choice


def hangman(word: str):
    """Function that handles main logic of program"""

    # creating list with single letters
    word_list, guesses = create_lists(word)
    tries_left = 6

    while True:

        # clearing console after each iteration for cleaner output
        clear_console()

        # showing game logo
        display_banner()

        # creating copy of guesses list for scoring purpose
        guesses_copy = guesses[:]
        # print(f'Tries left: {tries_left}')
        display_hangman(tries_left)

        # breaking the loop if no more tries are left
        if tries_left == 0:
            print('Game over mate')
            break

        # printing guessing progress
        display_guesses(guesses)

        # breaking the loop when user guess all letters
        if guesses == word_list:
            print('Congrats mate')
            break

        # asking user for guess, then checking if guess is correct
        check_guess(word_list, guesses)

        # if copy of guesses and guesses are equal
        # that means user didn't get letter right
        if guesses_copy == guesses:
            tries_left -= 1


def create_lists(word: str):
    """Function that takes single word as an argument
    and stores single letters in a list"""
    
    word = word.rstrip()
    word_list = [letter for letter in word]
    
    # a list where correct guesses will be stored
    guesses = [' ' for letter in word]

    return word_list, guesses


def display_guesses(guesses: list):
    """Function that will print guessed letters"""

    for letter in guesses:
        print(f'{letter}', end=' ')
    print()
    print('^ ' * len(guesses))
    

def check_guess(word_list: list, guesses: list):
    """Function that asks user for guess, 
    then checks if guess is correct"""
    
    guess = input('Type your guess: ')
    for index, letter in enumerate(word_list):
        if guess == letter:
            guesses[index] = guess


def display_banner():
    """Function that prints game logo"""

    banner = """
    
 ██░ ██ ▄▄▄      ███▄    █  ▄████ ███▄ ▄███▓▄▄▄      ███▄    █ 
▓██░ ██▒████▄    ██ ▀█   █ ██▒ ▀█▓██▒▀█▀ ██▒████▄    ██ ▀█   █ 
▒██▀▀██▒██  ▀█▄ ▓██  ▀█ ██▒██░▄▄▄▓██    ▓██▒██  ▀█▄ ▓██  ▀█ ██▒
░▓█ ░██░██▄▄▄▄██▓██▒  ▐▌██░▓█  ██▒██    ▒██░██▄▄▄▄██▓██▒  ▐▌██▒
░▓█▒░██▓▓█   ▓██▒██░   ▓██░▒▓███▀▒██▒   ░██▒▓█   ▓██▒██░   ▓██░
 ▒ ░░▒░▒▒▒   ▓▒█░ ▒░   ▒ ▒ ░▒   ▒░ ▒░   ░  ░▒▒   ▓▒█░ ▒░   ▒ ▒ 
 ▒ ░▒░ ░ ▒   ▒▒ ░ ░░   ░ ▒░ ░   ░░  ░      ░ ▒   ▒▒ ░ ░░   ░ ▒░
 ░  ░░ ░ ░   ▒     ░   ░ ░░ ░   ░░      ░    ░   ▒     ░   ░ ░  by Mati
 ░  ░  ░     ░  ░        ░      ░       ░        ░  ░        ░ 
                                                               
    """
    print(banner)


def display_hangman(tries_left):
    """Function that prints hangman string corresponding to the tries left"""

    hangman = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========",
    ]
    
    index = len(hangman) - tries_left - 1
    print(hangman[index])


def clear_console():
    """Function that clears the console window"""

    os.system('cls')


def main():
    """Main function"""

    # Open a file and store words in 'words' variable
    filename = 'hangman.txt'
    with open(filename) as file:
        # store words in a list by using 'readlines' method
        words = file.readlines()

    # main loop of the game
    # 'play_again' flag is used for continuing or breaking loop
    play_again = True
    while play_again:

        # picking random word from words list
        word = choice(words)
        hangman(word)

        # asking user if he wants to play again
        user_choice = input('Do you want to play again? (y/n): ').lower()
        if user_choice != 'y':
            play_again = False


if __name__ == '__main__':
    main()
