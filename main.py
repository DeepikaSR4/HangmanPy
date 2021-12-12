import random
import string
from words import words
from hangman import hangman

print("Hey!!!!!!! \n\n\t*******\nWelcome to HangmanPy\n\t*******\n\nPlease enter your name \n\t")
name = input()
print("Woah! \n Let's begin the game " + name, "\n\n")


def get_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangmanpy():
    word = get_word(words)
    letters_in_word = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    life = 10

    while len(letters_in_word) > 0 and life > 0:

        print(name, '!!!!!\n', life, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(hangman[life])
        print('\t\tCurrent word: ', ' '.join(word_list))

        using_letter = input('\t\tGuess a letter: ').upper()
        if using_letter in alphabet - used_letters:
            used_letters.add(using_letter)
            if using_letter in letters_in_word:
                letters_in_word.remove(using_letter)
                print('')

            else:
                life = life - 1
                print('\nYour letter,', using_letter, 'is not in the word.')

        elif using_letter in used_letters:
            print('\n', name, '!!!\t''you have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    if life == 0:
        print(hangman[life])
        print('You lost. The word was', word)
    else:
        print('\t************************\n\tYAY! \n\tYou guessed the word\n\t\t', word,
              '\n''\t************************\n')


if __name__ == '__main__':
    hangmanpy()
