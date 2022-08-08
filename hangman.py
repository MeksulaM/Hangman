from random import choice


def hangman(word: str):
    """Function that handles main logic of program"""

    # creating of list with single letters
    word = word.rstrip()
    word_list = [letter for letter in word]
    guesses = [' ' for letter in word]
    tries_left = 5

    while True:

        # creating copy of guesses list for scoring purpose
        guesses_copy = guesses[:]
        print(f'Tries left: {tries_left}')

        # printing guessing progress
        for letter in guesses:
            print(f'{letter}', end=' ')
        print()
        print('^ ' * len(word_list))

        # breaking loop when user guess all letters
        if guesses == word_list:
            print('Congrats mate')
            break

        # asking user for guess, then checking if guess is correct
        guess = input('Type your guess: ')
        for index, letter in enumerate(word_list):
            if guess == letter:
                guesses[index] = guess

        # if copy of guesses and guesses are equal
        # that means user didn't get letter right
        if guesses_copy == guesses:
            tries_left -= 1
            if not tries_left:
                print('Game over mate')
                break


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
        word = choice(words)
        hangman(word)
        user_choice = input('Do you want to play again? (y/n): ').lower()
        if user_choice != 'y':
            play_again = False


if __name__ == '__main__':
    main()
