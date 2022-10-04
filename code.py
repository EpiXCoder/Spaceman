import random
from colorama import Fore 

def load_word():
    '''
    A function that reads a text file and randomly selects a word (also referred to as secret word) 
    from the list to be used per iteration of the game. It also splits the word into letters.
    Returns: 
        array: A list containing each of the letters of the secret word.
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') 
    selected_word = random.choice(words_list)
    secret_word = list(selected_word)
    # print (secret_word)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True
        
def get_guessed_word(secret_word, letters_guessed, hidden_word):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
        hidden_word (list of string): List of letters (that have been guessed) and underscores (for letters that have not been guessed)
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    i = 0
    while i < len(secret_word):
        if secret_word[i] in letters_guessed:
            hidden_word[i] = secret_word[i]
        i += 1

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word.
    It also appends letters to two lists: one with correctly guessed letters and another with wrongly guessed letters.
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    if guess in secret_word:
        correct_guess.append(guess)
        return True
    else:
        wrong_guess.append(guess) 
        return False

def guessed (guess, secret_word):
    '''
    A function that appends guessed letters to a list
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    '''
    letters_guessed.append(guess)

def draw_man (wrong_guess):
    '''
    A function that draws the ASCII 'space man'
    Args:
        wrong_guess (list of strings): A list with letters guessed wrong so far
    '''
    colors = dict(Fore.__dict__.items())
    if len(wrong_guess) == 1 :
        print(colors['GREEN']+ ' 👽')
    elif len(wrong_guess) == 2 :
        print(colors['GREEN']+ ' 👽\n⎧')
    elif len(wrong_guess) == 3 :
        print(colors['GREEN']+ ' 👽\n⎧(')
    elif len(wrong_guess) == 4 :
        print(colors['GREEN']+ ' 👽\n⎧()')
    elif len(wrong_guess) == 5 :
        print(colors['GREEN']+ ' 👽\n⎧()⎫')
    elif len(wrong_guess) == 6 :
        print(colors['GREEN']+ ' 👽\n⎧()⎫\n ⌋')
    elif len(wrong_guess) == 7 :
        print(colors['GREEN']+ ' 👽\n⎧()⎫\n ⌋⌊')



def user_input(prompt):
    '''
    A function that creates a proxy variable for the user input using prompt
    Args:
        prompt(string): a string with the question displayed to the user
    Returns:
        string: the entry input by the user (one letter at a time)
    '''
    user_input = input(prompt)
    return user_input

def opener(secret_word, hidden_word):
    '''
    A function that displays the welcome message and the game rules.
    Args:
        secret_word (string): the random word the user is trying to guess.
        hidden_word (list of string): List of letters (that have been guessed) and underscores (for letters that have not been guessed)
    '''
    colors = dict(Fore.__dict__.items())
    print()
    print()
    print(colors['WHITE']+'*****************************')
    welcomeMessage = 'WELCOME to SPACE MAN\n'

    for character in welcomeMessage:
        print(colors[random.choice(list(colors.keys()))] + character, end='')

    print(colors['GREEN']+ ' 👽\n⎧()⎫\n ⌋⌊')
    print(colors['WHITE']+'*****************************')
    print()
    print(colors['CYAN'] + "RULES OF THE GAME:\n- You will be guessing the secret word one letter at a time.\n- You will only have 7 strikes if you guess the wrong letters.\n- Guess the secret word corretly before the spaceman is built to completion.\n- Ready? Let's Go!")
    print()
    print(colors['WHITE'] + "Secret Word has " + str(len(secret_word)) + " letters.")
    print(colors['YELLOW'] + "The Secret Word: " + (' '.join(hidden_word)))
    print(colors['WHITE']+'*****************************')
    print()

def closer(secret_word, letters_guessed):
    '''
    A function that displays whether the user won or lost. Also provides some closing remarks.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    '''
    colors = dict(Fore.__dict__.items())
  
    print(colors['WHITE']+'*****************************')
    if is_word_guessed (secret_word, letters_guessed):
        print(colors['GREEN'] + "CONGRATULATIONS! You win! You've guessed the word correctly!")
        print(colors['GREEN'] + "The secret word was: " + (''.join(secret_word)))
        
    else:
        print (colors['RED'] + "Sorry! You lose. You did not guess the word correctly!")
        print (colors['GREEN'] + "The secret word was: " + (''.join(secret_word)))

    print(colors['WHITE']+'*****************************')

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman
    Args:
        Secret_word: a list of string containing the letter of the secret word. 
    '''
    colors = dict(Fore.__dict__.items())
    
    opener(secret_word, hidden_word)
    
    run = True

    while run or len(wrong_guess) <= 7:
        if len(wrong_guess) == 7 and run ==True:
            print ()
            print (colors['RED'] + "OH NO! You've run out of guesses.")
            print ()
            break

        guess = user_input(colors['CYAN'] + "Enter guess one letter at a time: ")
        while len(guess) != 1 or guess.isalpha() == False or guess.strip() == '':
            print()
            print (colors['RED'] + "Invalid Entry.")
            print()
            guess = user_input(colors['CYAN'] + "Enter guess one letter at a time: ")

        while guess in hidden_word or guess in letters_guessed:
            print ()
            print (colors['RED'] + "You've already guessed '" + str(guess) + "'!")
            print ()
            guess = user_input(colors['CYAN'] + "Enter guess one letter at a time: ")
        
        print ()
        if is_guess_in_word(guess, secret_word):
            guessed (guess, secret_word)
            get_guessed_word(secret_word, letters_guessed, hidden_word)
            print (colors['GREEN'] + "Great!! '" + str(guess) + "' is in the secret word.")
        else: 
            guessed (guess, secret_word)
            print (colors['RED'] + "Sorry! '" + str(guess) + "' is not in the secret word.")
        
        print ()
        print(colors['WHITE']+'*****************************')
        print ()

        draw_man (wrong_guess)

        print ()
        print(colors['YELLOW'] + "The Secret Word: " + (' '.join(hidden_word)))
        print(colors['WHITE'] + "Correct letters guessed so far: " + (','.join(correct_guess)))
        print(colors['WHITE'] + "Wrong letters guessed so far: " + (','.join(wrong_guess)))
        print(colors['WHITE'] + "Wrong guesses left: " + str(7 - len(wrong_guess)))
        print()
        
        if is_word_guessed(secret_word, letters_guessed):
            run = False
        if run == False:
            break


# --------------------------------------------------------------------------------
# START GAME!
# --------------------------------------------------------------------------------

#loading word
secret_word = load_word()

#Initiating variables and and lists
secret_word_joint = ''.join(secret_word)
hidden_word = list(len(secret_word) * '_')
letters_guessed = []
correct_guess = []
wrong_guess = []

#Calling game comtrolling function
spaceman(secret_word)

#Calling closer function that announces if the game was won or lost
closer(secret_word, letters_guessed)

