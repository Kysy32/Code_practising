import random
import os

import words
import figurine


SEPARATOR = '=' * 45

def introduction ():
    '''
    Print introduction and basic rules
    '''
    print(f'Welcome to our game Hangman!!!\n'
          f'The aim of this game is find secret word.\n'
          f'You can quess one later or the whole word.\n'
          f'You have 7 attempts so good luck :)\n'
          f'{SEPARATOR}')

def generate_random_word():
    '''
    Generate random word form list of words.
    '''
    word = random.choice(words.all_words)
    return word

def create_secret(word):
    '''
    Generate symbol '_' for every letter in secret word
    '''
    secret = len(word) * ['_']
    return secret

def drawing_gallows(actaul_lives):
    '''
    Printing actual faze of gallows
    '''
    gallows = figurine.hangman[7 - actaul_lives]
    return gallows

def guessing():
    '''
    Asking users for their tips
    '''
    user_input = input('Guess the letter or word: ')
    return user_input

def game_ending(actual_lives, word):
    '''
    Decides if player win or lose
    '''
    if not actual_lives:
        print(
              f"You lose, maybe next time :).",
              f"Secret word was: {word}.",
              sep="\n")
    else:
        print(f"Secret word: {word}",
              "Congratulation to win :)!",
              sep="\n")


def hangman():
    word = generate_random_word()
    secret = create_secret(word)
    actual_lives = 7
    #print(word)
    game = True


    while game and actual_lives > 0:
        os.system("cls")
        print(' '.join(secret))
        figurine = drawing_gallows(actual_lives)
        print(figurine)
        tip = guessing()

        if tip == word:
            print(f'That is correct secret word is {word}\n'
                  f'You win this round')
            game = False

        elif len(tip) == 1 and tip in word:
            print(f'You guessed the letter')
            for index, latter in enumerate(word):
                if latter == tip:
                    secret[index] = tip

            if "_" not in secret:
                print('You win :)')
                game = False
        else:
            actual_lives -= 1
            if actual_lives == 0:
                print(word)

    else:
        os.system("cls")
        final_figurine = drawing_gallows(actual_lives)
        print(final_figurine)
        game_ending(actual_lives,word)

def main():
    '''
    Start the game Hangman
    '''
    introduction()
    hangman()


main()