

def main():
    """Main function"""

    # Open a file and store words in 'words' variable
    filename = 'hangman.txt'
    with open(filename) as file:
        # store words in a list by using 'readlines' method
        words = file.readlines()


if __name__ == '__main__':
    main()