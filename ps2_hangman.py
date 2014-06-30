# 6.00 Problem Set 3
#
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

# 1.) Display the word as blank letters
# 2.) Ask the user to input a guess
# 3.) Check to see if the guess matches one of the letters in the word
#  - Valid guesses are unguessed letters
# 4.) If correct, display word with letter filled in
# 5.) If incorrect, take away a guess
# 6.) Remove guessed letter from available guesses
# 7.) Display word with correct guesses filled in and # guesses remaining.
# 8.) When the user runs out of guesses, they lose.
# 9.) When the user guesses the word, they win!

# write a function to build a string with the guessed letters
# write a function to display unused letters

def hide_word(word):
  hidden_word = ""
  for w in word:
    hidden_word += "_"
  return hidden_word


def check_letters(letters,guess):
  for l in letters:
    if guess == l:
      letters = letters.replace(guess, "")
      return letters
    else:
      print "That is not a valid guess! Try again."
#       ask()
#
#
# def ask():
#   return str(raw_input("Pick a letter: "))





def check_guess(guess, hidden_word, word, letters):
  hidden_word_list = list(hidden_word)
  index = 0
  for w in word:
    if guess == w:
      hidden_word_list[index] = w
    index += 1
  hidden_word = ''.join(hidden_word_list)
  return (hidden_word, word)


word = choose_word(wordlist)
hidden_word = hide_word(word)
length = len(word)
guess_count = 10
letters = 'bcdefghijklmnopqrstuvwxyz'

print "Welcome to the game, hombre."
print "I have chosen a word that is", length, "letters long."
print "The word is: ", hidden_word
print "------------------------------"
print "You have ", guess_count, " guesses left."

guess = ask()
print check_letters(letters,guess)
# print check_guess(guess, hidden_word, word, letters)
