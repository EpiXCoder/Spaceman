import random

# from colored import fg

from colorama import Fore 

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') 
    selected_list = []
    for word in words_list:
        if len(word) <= 7:
            selected_list.append(word)
    selected_word = random.choice(selected_list)
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
        
    #TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    #pass

# print(is_word_guessed(secret_word, letters_guessed))


def get_guessed_word(secret_word, letters_guessed, hidden_word):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    i = 0
    while i < len(secret_word):
        if secret_word[i] in letters_guessed:
            hidden_word[i] = secret_word[i]
        i += 1


# get_guessed_word(secret_word, letters_guessed,hidden_word)
# print(hidden_word)
# print(''.join(hidden_word))

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    if guess in secret_word:
     return True
    else: 
        return False



    #TODO: check if the letter guess is in the secret word
def guessed (guess):
    letters_guessed.append(guess)


# print (is_guess_in_word(guess, secret_word))

# welcomeMessage = 'WELCOME to SPACE MAN'

def user_input(prompt):
    user_input = input(prompt)
    return user_input




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    colors = dict(Fore.__dict__.items())
    starBorder = '*****************************\n'
    for character in starBorder:
        print(colors[random.choice(list(colors.keys()))] + character, end='')
    welcomeMessage = 'WELCOME to SPACE MAN\n'
    for character in welcomeMessage:
        print(colors[random.choice(list(colors.keys()))] + character, end='')
    for character in starBorder:
        print(colors[random.choice(list(colors.keys()))] + character, end='')
   
    print(colors['CYAN'] + "RULES OF THE GAME:\n- You will be guessing the secret word one letter at a time\n- You will have 7 attempts to guess the word correctly.\n- Ready? Let's Go!")
    print()
    print(colors['GREEN'] + "Secret Word has " + str(len(secret_word)) + " letters.")
    print(colors['GREEN'] + "The Secret Word: " + (' '.join(hidden_word)))
    print()
    guess_left = 7
    run = True
    while run or guess_left > 0:
        if guess_left == 0 and run ==True:
            print ()
            print (colors['RED'] + "OH NO! You've run out of guesses.")
            print ()
            break

        guess = user_input(colors['BLUE'] + "Enter guess one letter at a time: ")
        while len(guess) != 1 or guess.isalpha() == False or guess.strip() == '':
            print(' ')
            print (colors['RED'] + "Invalid Entry.")
            print(' ')
            guess = user_input(colors['BLUE'] + "Enter guess one letter at a time: ")

        while guess in hidden_word or guess in letters_guessed:
            print ()
            print (colors['RED'] + "You've already guessed '" + str(guess) + "'!")
            print ()
            guess = user_input(colors['BLUE'] + "Enter guess one letter at a time: ")
        
        guess_left -= 1
        print ()
        if is_guess_in_word(guess, secret_word):
            guessed (guess)
            get_guessed_word(secret_word, letters_guessed, hidden_word)
            print (colors['GREEN'] + "Great!! '" + str(guess) + "' is in the secret word.")
        else: 
            guessed (guess)
            print (colors['RED'] + "Sorry! '" + str(guess) + "' is not in the secret word.")
        
        print ()
        print(colors['GREEN'] + "The Secret Word: " + (' '.join(hidden_word)))
        print(colors['YELLOW'] + "Letters guessed so far: " + (','.join(letters_guessed)) )
        print(colors['YELLOW'] + "Guesses left: " + str(guess_left) )
        if is_word_guessed(secret_word, letters_guessed):
            run = False
        if run == False:
            break


# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# START GAME!

secret_word = load_word()
# secret_word = ['a', 'p', 'p', 'l', 'e']
secret_word_joint = ''.join(secret_word)
hidden_word = list(len(secret_word) * '_')
letters_guessed = [ ]
    
spaceman(secret_word)

colors = dict(Fore.__dict__.items())
starBorder = '*****************************\n'
for character in starBorder:
    print(colors[random.choice(list(colors.keys()))] + character, end='')

if is_word_guessed (secret_word, letters_guessed):
    print(colors['GREEN'] + "CONGRATULATIONS! You win! You've guessed the word correctly!")
    print(colors['GREEN'] + "The secret word was: " + (''.join(secret_word)))
    
else:
    print (colors['RED'] + "Sorry! You lose. You did not guess the word correctly!")
    print (colors['GREEN'] + "The secret word was: " + (''.join(secret_word)))

for character in starBorder:
    print(colors[random.choice(list(colors.keys()))] + character, end='')

  






