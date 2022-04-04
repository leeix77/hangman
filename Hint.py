import hangman1 as hm
import random


secret_word = hm.secret_word
letters_guessed = hm.letters_guessed
get_available_letters = hm.get_available_letters
get_guessed_word = hm.get_guessed_word
class hint:
    def __init__(self):
        print('Oops, you now meet trouble')
        print('You can use any hint to help you out')
        print('But you are encouraged to finish the problem yourself')
        call=input('''Here is the hint you can call for:
         'dele' for deleting a wrong letter from available letters
         'show()' for showing one letter in the word
         cheat for showing the answer''')
        if call=='dele':
            hint.dele()
        if call=='show':
            hint.show(secret_word,letters_guessed)
        if call=='cheat':
            hint.cheat()
        
    def dele(secret_word,letters_guessed):
        my_list=[]
        for i in range(len(get_available_letters(letters_guessed+list(secret_word)))):
            my_list.append(get_available_letters(letters_guessed+list(secret_word))[i])
        my_list.pop(random.randint(0,len(my_list)-1))
        return my_list
    def show(secret_word,letters_guessed):
        secret_word_list=[]
        words_ready_to_show=[]
        for i in range(len(secret_word)):
            secret_word_list.append (secret_word[i])
        for i in range(len(secret_word_list)):
            if secret_word_list[i] not in letters_guessed:
                words_ready_to_show.append(secret_word_list[i])
        letters_guessed=words_ready_to_show[random.randint(0,len(words_ready_to_show)-1)]
        print(get_guessed_word(secret_word,letters_guessed))

    def cheat():
        print(secret_word)
