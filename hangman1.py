# Problem Set 2, hangman.py
# Name: Jingran Cao
# Collaborators: Kenneth Pak, Lei Xu
# Time spent:8h

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    try:
    # Open file in read-only mode
        inFile = open(WORDLIST_FILENAME, 'r')
    except IOError as e:
        print("An error occurred:", e)
#     inFile = open(WORDLIST_FILENAME, 'r')
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
    secret_word=random.choice(wordlist)
    return secret_word

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
secret_word=choose_word(wordlist)
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    a=1
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
                   a=a*1
        else:
                   a=a*0
    return bool(a)


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    underscores='_'*(len(secret_word))
    guessed_word_listtype=list(underscores)
    guessed_word=''
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            guessed_word_listtype[i]=secret_word[i]
        if i<len(secret_word)-1:
                guessed_word=guessed_word+guessed_word_listtype[i]+' '
        if i==len(secret_word)-1:
                guessed_word=guessed_word+guessed_word_listtype[i]
    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_letters_list=list('abcdefghijklmnopqrstuvwxyz')
    available_letters=''
    for i in range(len(all_letters_list)):
        if all_letters_list[i] not in letters_guessed:
            available_letters=available_letters+all_letters_list[i]
    return available_letters
            

letters_guessed=[]
import Hint as hint

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    print("Welcome to hangman o(≧▽≦*)o!")
    print("I am thinking of a word that is " +str(len(secret_word))+" letters long.")
    print('You have 6 guesses left.')
    print('Available letters: '+'abcdefghijklmnopqrstuvwxyz')
    print('You should guess only one letter at a time')
    print('-----------------------------------------------')
    
    def chances_left(letters_guessed):
        return 6-len(letters_guessed)
    
    while chances_left(letters_guessed)>0:
        
        guess=input('Please enter your guess: ')
        def only_alphabet( x ):  
            case_1 = x not in ['cheat', 'show', 'dele']
            case_2 = x not in ('abcdefghijklmnopqrstuvwxyz')
            if case_1 and case_2: 
                raise Exception("Invalid input!")         # when abnoral detected
        try:    
            only_alphabet(guess)            # cast abnormal
        except Exception:     
            print("please input one lower case letter")
            continue
        def control_length(x):
            case_1 = x not in ['cheat', 'show', 'dele']
            case_2 = len(str(x))>1
            if case_1 and case_2:
                raise Exception("please input only one lower case letter")
        try:    
            control_length(guess)            # cast abnormal
        except Exception:     
            print("please input one lower case letter")
            continue
        if guess == "cheat":
                hint.hint.cheat()
                print('You cheated, but you win')
                break
        if guess == 'show':
            hint.hint.show(secret_word,letters_guessed)
            continue
        if guess == 'dele':
            print('You have '+str(chances_left(letters_guessed))+' chances left')
            print(get_guessed_word(secret_word,letters_guessed))
            print('Available letters: '+"".join(hint.hint.dele(secret_word,letters_guessed)))
            print('-----------------------------------------------------')
            continue
        '''
        if len(guess)>1:
            print('Please enter only one letter at a time.')
            print('You have '+str(chances_left(letters_guessed))+' chances left')
            print(get_guessed_word(secret_word,letters_guessed))
            print('Available letters: '+get_available_letters(letters_guessed))
            print('-----------------------------------------------------')
            continue
        if guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please only enter English letters')
            print('You have '+str(chances_left(letters_guessed))+' chances left')
            print(get_guessed_word(secret_word,letters_guessed))
            print('Available letters: '+get_available_letters(letters_guessed))
            print('-----------------------------------------------------')
            continue
        if guess=='':
            print('Please enter something.')
            print('You have '+str(chances_left(letters_guessed))+' chances left')
            print(get_guessed_word(secret_word,letters_guessed))
            print('Available letters: '+get_available_letters(letters_guessed))
            print('-----------------------------------------------------')
            continue
        '''
        if guess in letters_guessed:
            print("You have already guessed this letter.") 
            print('You have '+str(chances_left(letters_guessed))+' chances left')
            print(get_guessed_word(secret_word,letters_guessed))
            print('Available letters: '+get_available_letters(letters_guessed))
            print('-----------------------------------------------------')
            continue
        else:
            letters_guessed.append(guess)
        
            if is_word_guessed==True:
                print('Congratulations, you win!o(≧▽≦*)o')
                break 
            if chances_left(letters_guessed)==0:
                print('You lose, better luck next time!')
                break
            if guess in secret_word:
                print('Nice!')
            else:
                print('Sorry, wrong guess')
            print('You have '+str(chances_left(letters_guessed))+' chances left')
            print(get_guessed_word(secret_word,letters_guessed))
            print('Available letters: '+get_available_letters(letters_guessed))
            print('-----------------------------------------------------')
        
