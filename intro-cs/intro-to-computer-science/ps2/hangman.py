# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
vowels = 'aeio'


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    guessed = True

    for character in secret_word:
        if  character not in letters_guessed:
            guessed = False
            break

    return guessed

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ''
    for character in secret_word:
        if character in letters_guessed:
            guessed_word += character + ' '
        else:
            guessed_word += '_ '

    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = ''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for character in string.ascii_lowercase:
        if character not in letters_guessed:
            available_letters += character

    return available_letters

def is_valid_input(input, letters_guessed):
    if len(input) > 1:
        return False
    if input in letters_guessed:
        return False
    if not str.isalpha(input):
        return False

    return True

def get_warning_message(input, letters_guessed):
    if len(input) > 1:
        return "Oops! You should write only one letter."
    if input in letters_guessed:
        return "Oops! You've already guessed that letter."
    if not str.isalpha(input):
        return "Oops! That is not a valid letter."

    return None
        

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    guesses_left = 6
    warnings_left = 3

    print("Welcome to the game Hangman")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("-------------")

    while True:
        print(f"You have {guesses_left} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")

        letter = str.lower(input("Please guess a letter: ")) 

        if letter == '*':
            print(f"Possible word matches are: {show_possible_matches(get_guessed_word(secret_word, letters_guessed))}")
            print("------------")
            continue

        warning = get_warning_message(letter, letters_guessed)

        if warning:
            warnings_left -= 1
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            info = f"You have {warnings_left} warnings. {guessed_word}"

            if warnings_left < 0:
                info = f"You have no warnings left so you lose one guess: {guessed_word}"
                warnings_left = 3
                guesses_left -= 1

            print(f"{warning} {info}")
        elif letter in secret_word:
            letters_guessed.append(letter)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            print(f"Good guess: {guessed_word}")
        else:
            if letter in vowels:
                guesses_left -= 2
            else:
                guesses_left -= 1

            letters_guessed.append(letter)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            print(f"Oops! That letter is not in my word: {guessed_word}")

        print("------------")

        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses_left * len(set(list(secret_word)))
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {total_score}")
            break

        if guesses_left == 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}")
            break



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    guess_word = my_word.strip().split()

    if len(guess_word) != len(other_word):
        return False

    invalid_characters = []

    match = True

    for index, character in enumerate(guess_word):
        if character == '_':
            invalid_characters.append(other_word[index])
        elif character != other_word[index]:
            match = False
            break
        elif character in invalid_characters and character == other_word[index]:
            match = False
            break

    return match

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    words = ''
    for word in wordlist:
        if match_with_gaps(my_word, word):
            words += ' ' + word

    if not words:
        return "No matches found"

    return words
        
if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)