import os
from random import choice


def hangman(word: str):
    """Function that handles main logic of program"""

    # creating list with single letters
    word_list, guesses, wrong_letters = create_lists(word)

    # user has 'tries_left' tries to guess all letters
    tries_left = 6

    while True:

        # clearing console after each iteration for cleaner output
        clear_console()

        # showing game logo
        display_banner()

        # creating copy of guesses list for scoring purpose
        guesses_copy = guesses[:]

        # print hangman ascii
        display_hangman(tries_left)

        # breaking the loop if no more tries are left
        if game_over(tries_left, word_list):
            break

        # printing guessing progress
        display_guesses(guesses)
        
        # printing wrong letters
        display_wrong_letters(wrong_letters)
        
        # breaking the loop when user guess all letters
        if word_is_guessed(guesses, word_list):
            break

        # asking user for guess, then checking if guess is correct
        check_guess(word_list, guesses, wrong_letters)

        # check if tries_left have to be updated
        tries_left = update_tries_left(tries_left, guesses_copy, guesses)


def create_lists(word: str):
    """Function that takes single word as an argument
    and stores single letters in a list"""
    
    word = word.rstrip()
    word_list = [letter for letter in word]
    
    # a list where correct guesses will be stored
    guesses = [' ' for letter in word]
    
    # a list whrere wrong letters will be stored
    wrong_lett = list()

    return word_list, guesses, wrong_lett


def display_guesses(guesses: list):
    """Function that will print guessed letters"""

    for letter in guesses:
        print(f'{letter}', end=' ')
    print()
    print('^ ' * len(guesses))
    

def check_guess(word_list: list, guesses: list, wrong_letters: list):
    """Function that asks user for guess, 
    then checks if guess is correct"""
    
    guess = user_input_validation()
    for index, letter in enumerate(word_list):
        if guess == letter:
            guesses[index] = guess
    
    add_wrong_letter_to_list(word_list, guess, wrong_letters)


def user_input_validation():
    """Function that checks if user input is valid"""

    #     
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    guess = input('\nType your guess: ').upper()
    
    # making sure user inputs single letter
    if len(guess) != 1:
        print('Wrong input mate')
        return user_input_validation()

    # making sure user inputs letter'
    if guess not in letters:
        print('Wrong input mate')
        return user_input_validation()
    
    return guess


def add_wrong_letter_to_list(word_list: list, guess: str, wrong_letters: list):
    """Function that adds wrong letter to wrong letters list"""
    
    if guess not in word_list and guess not in wrong_letters:
        wrong_letters.append(guess)


def display_wrong_letters(wrong_letters: list):
    """Function that prints wrong letters"""

    if wrong_letters:
        print('\nWrong letters:')
        for letter in wrong_letters:
            print(letter, end=' ')
        print()

def game_over(tries_left: int, word_list: list):
    """Function that prints game over message and will break the loop"""

    if tries_left == 0:
        display_guesses(word_list)
        print('\nGame over mate')
        return True
    else:
        return False


def word_is_guessed(guesses: list, word_list: list):
    """Function that checks if user guessed all letters
        If yes, function will break the loop"""

    if guesses == word_list:
        print('\nCongrats mate')
        return True
    else:
        return False


def update_tries_left(tries_left: int, guesses_copy: list, guesses: list):
    """Function that updates tries left if user guess was wrong"""

    # if copy of guesses and guesses are equal
    # that means user didn't get letter right
    if guesses_copy == guesses:
        tries_left -= 1
    
    return tries_left


def display_banner():
    """Function that prints game logo"""

    # ascii art
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

    # ascii hangman art
    hangman_strings = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========\n", 
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========\n",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========\n",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========\n", 
        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========\n",
        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========\n",
        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========\n",
    ]
    
    index = len(hangman_strings) - tries_left - 1
    print(hangman_strings[index])


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
