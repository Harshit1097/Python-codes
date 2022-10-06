# Guess the complete word with limited number of lives
import random
from words import words
import string

# computer chooses a random word from a list of words given in words.py file


def get_valid_word(words):

    # this function keeps choosing a word randomly from the words list until we get a word that is
    # without '-' or space in between

    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman(words):
    correct_word = get_valid_word(words)
    used_letters = set()                        # stores the letters guessed by user
    word_letters = set(correct_word)            # set of all letters in the correct_word
    alphabets = set(string.ascii_uppercase)     # set of all 26 upper case alphabets

    lives = 7

    while len(word_letters) > 0 and lives != 0:

        print(f"lives left = {lives}")
        print("You have used these letters: ", " ".join(used_letters))

        # printing the current word
        word_list = [letter if letter in used_letters else "-" for letter in correct_word]
        print("Current word: ", ' '.join(word_list))

        alpha = input("\nGuess a letter: ").upper()

        if alpha in (alphabets - used_letters):
            used_letters.add(alpha)
            if alpha in word_letters:
                word_letters.remove(alpha)
            else:
                lives -= 1
                print('Letter is not in the word!')

        elif alpha in used_letters:
            print("You've already tried this letter!")

        else:
            print("Wrong character typed! Enter valid character.")

    if lives != 0:
        return f"You have correctly guessed the word {correct_word}"

    return f"You are out of lives! The word is {correct_word}"


print(hangman(words))
