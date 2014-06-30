# 6.00 Problem Set 3
#
# Hangman
#

# Problem Set 2
# Name: CZ
# Collaborators (Discussion): --
# Collaborators (Identical Solution): --
# Time: 0:30 (Sunday night)
# Time: 0:45 (Monday)
# Notes: Started outlining on Sunday night. Fell onto the other side of
#        the Ballmer Peak. Picked it up Monday, completed fine.
#        Extra time Monday mostly for formatting/polish
# Beers: 5 (Sunday) 0 (Monday)



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

def hide_word(word):
  """ Takes the computer's selected word and replaces each character
      with an underscore. Returns a new value """
  hidden_word = ""
  for w in word:
    hidden_word += "_"
  return hidden_word


def summary(hidden_word, guess_count):
  """ Provides the status of the game so far, revealing guessed letters
      and the number of guesses and letters left """
  print ""
  print "------------------------------"
  print "The word is", hidden_word
  print "Guesses left:", guess_count
  print "Available letters are: ", letters


def check_letters(letters,guess):
  """ Checks the guess against the string of available remaining letters
      and makes sure only a single letter has been guessed. Removes
      guessed letters from valid letters string """
  for l in letters:
    if letters.find(guess) != -1 and len(guess) == 1:
      letters = letters.replace(guess, "")
      return letters, True
    else:
      return letters, False


def check_guess(guess, hidden_word, word):
  """ Checks to see if guess is correct. If correct, replaces underscores in
      hidden word with guesses letter, then returns the word appropriately
      filled in """
  hidden_word_list = list(hidden_word)
  index = 0
  for w in word:
    if guess == w:
      hidden_word_list[index] = w
    index += 1
  hidden_word = ''.join(hidden_word_list)
  if word.find(guess) != -1:
    return hidden_word, True
  else:
    return hidden_word, False


word = choose_word(wordlist)
hidden_word = hide_word(word)
length = len(word)
guess_count = 10
letters = 'abcdefghijklmnopqrstuvwxyz'

print "Welcome to the game, hombre."
print "I have chosen a word that is", length, "letters long."
summary(hidden_word, guess_count)
while hidden_word != word and guess_count > 0:
  guess = str(raw_input("Guess a letter:"))
  letters, valid = check_letters(letters,guess)
  if valid == False:
    print "That is not a valid guess. Try again."
  else:
    hidden_word, correct = check_guess(guess, hidden_word, word)
    if correct == False:
      guess_count -= 1
      print "Sorry, that letter isn't in the word."
    else:
      print "Good guess!"
  if guess_count == 0 or hidden_word == word:
    break
  summary(hidden_word, guess_count)
if guess_count == 0:
  print "YOU LOSE! The word was:", word
elif hidden_word == word:
  print "YOU WIN!"
