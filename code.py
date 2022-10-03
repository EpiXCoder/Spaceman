import random
from colorama import Fore 

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') 
    selected_word = random.choice(words_list)
    secret_word = list(selected_word)
    # print (secret_word)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True
        
def get_guessed_word(secret_word, letters_guessed, hidden_word):
    i = 0
    while i < len(secret_word):
        if secret_word[i] in letters_guessed:
            hidden_word[i] = secret_word[i]
        i += 1

def is_guess_in_word(guess, secret_word):
    if guess in secret_word:
        correct_guess.append(guess)
        return True
    else:
        wrong_guess.append(guess) 
        return False

def guessed (guess, secret_word):
    letters_guessed.append(guess)

def draw_man (wrong_guess):
    colors = dict(Fore.__dict__.items())
    if len(wrong_guess) == 1 :
        print(colors['GREEN']+ ' 👽')
    elif len(wrong_guess) == 2 :
        print(colors['GREEN']+ ' 👽')
        print(colors['GREEN']+ '⎧')
    elif len(wrong_guess) == 3 :
        print(colors['GREEN']+ ' 👽')
        print(colors['GREEN']+ '⎧(')
    elif len(wrong_guess) == 4 :
        print(colors['GREEN']+ ' 👽')
        print(colors['GREEN']+ '⎧()')
    elif len(wrong_guess) == 5 :
        print(colors['GREEN']+ ' 👽')
        print(colors['GREEN']+ '⎧()⎫')
    elif len(wrong_guess) == 6 :
        print(colors['GREEN']+ ' 👽')
        print(colors['GREEN']+ '⎧()⎫')
        print(colors['GREEN']+ ' ⌋')
    elif len(wrong_guess) == 7 :
        print(colors['GREEN']+ ' 👽')
        print(colors['GREEN']+ '⎧()⎫')
        print(colors['GREEN']+ ' ⌋⌊')


    # print(colors['GREEN']+ ' 👽')
    # print(colors['GREEN']+ '⎧()⎫')
    # print(colors['GREEN']+ ' ⌋⌊')

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
    print(colors['WHITE']+'*****************************')
    welcomeMessage = 'WELCOME to SPACE MAN\n'
    for character in welcomeMessage:
        print(colors[random.choice(list(colors.keys()))] + character, end='')
    print(colors['GREEN']+ ' 👽')
    print(colors['GREEN']+ '⎧()⎫')
    print(colors['GREEN']+ ' ⌋⌊')
    print(colors['WHITE']+'*****************************')
    print()
    print(colors['CYAN'] + "RULES OF THE GAME:\n- You will be guessing the secret word one letter at a time.\n- You will only have 7 strikes if you guess the wrong letters.\n- Guess the secret word corretly before the spaceman is built to completion.\n- Ready? Let's Go!")
    print()
    print(colors['WHITE'] + "Secret Word has " + str(len(secret_word)) + " letters.")
    print(colors['YELLOW'] + "The Secret Word: " + (' '.join(hidden_word)))
    print()
    run = True
    while run or len(wrong_guess) <= 7:
        if len(wrong_guess) == 7 and run ==True:
            print ()
            print (colors['RED'] + "OH NO! You've run out of guesses.")
            print ()
            break

        guess = user_input(colors['CYAN'] + "Enter guess one letter at a time: ")
        while len(guess) != 1 or guess.isalpha() == False or guess.strip() == '':
            print(' ')
            print (colors['RED'] + "Invalid Entry.")
            print(' ')
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
# --------------------------------------------------------------------------------
# START GAME!

secret_word = load_word()

secret_word_joint = ''.join(secret_word)
hidden_word = list(len(secret_word) * '_')
letters_guessed = []
correct_guess = []
wrong_guess = []

# print (secret_word)
spaceman(secret_word)
colors = dict(Fore.__dict__.items())
print(colors['WHITE']+'*****************************')
if is_word_guessed (secret_word, letters_guessed):
    print(colors['GREEN'] + "CONGRATULATIONS! You win! You've guessed the word correctly!")
    print(colors['GREEN'] + "The secret word was: " + (''.join(secret_word)))
    
else:
    print (colors['RED'] + "Sorry! You lose. You did not guess the word correctly!")
    print (colors['GREEN'] + "The secret word was: " + (''.join(secret_word)))

print(colors['WHITE']+'*****************************')
