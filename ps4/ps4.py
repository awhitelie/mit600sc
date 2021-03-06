# 6.00 Problem Set 4
#
# Caesar Cipher Skeleton
#


import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
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
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


# (end of helper code)
# -----------------------------------

#
# Problem 1: Encryption
#
def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_coder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)
    """
    ### TODO.

    assert shift >= 0 and shift < 27, "shift %s is not between 0 and 27."

    upper_alpha = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                   'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                   'X', 'Y', 'Z']
    lower_alpha = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                   'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                   'x', 'y', 'z']
    old = upper_alpha + lower_alpha

    # looking at the solutions file, instead of manually typing in the set you can use:
    # string.ascii_lowercase + ' '
    # string.ascii)uppercase + ' '


    new_upper = shift_alpha(upper_alpha, shift)
    new_lower = shift_alpha(lower_alpha, shift)
    new = new_upper + new_lower

    coder = dict(zip(old,new))
    return coder

def shift_alpha(alpha, shift):
  ''' Shifts an alphabet the specified number of characters-- wraps around
      so that the last letter becomes the first, etc '''

  # shifted = []
  #
  # for i in range(len(alpha)):
  #   shifted.append(alpha[shift])
  #   shift += 1
  #   if shift > 26:
  #     shift = 0

  shifted = alpha[shift:] + alpha[:shift]

  return shifted


# ----------------------
# Test for build_coder()
# ----------------------

# build_coder(5)

# ----------------------


def build_decoder(shift):
    """
    Returns a dict that can be used to decode an encrypted text. For example, you
    could decrypt an encrypted text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    >>>decrypted_text = apply_coder(plain_text, decoder)

    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_decoder(3)
    {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
    'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
    'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
    'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
    'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
    'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
    'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
    'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    ### TODO.
    assert shift >= 0 and shift < 27, 'shift %s is not between 0 and 27.'

    return build_coder(27 - shift)

# ----------------------
# Test for build_decoder()
# ----------------------

# print build_decoder(3)

# ----------------------


def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Example:
    >>> apply_coder("Hello, world!", build_coder(3))
    'Khoor,czruog!'
    >>> apply_coder("Khoor,czruog!", build_decoder(3))
    'Hello, world!'
    """
    new_text = ''
    for t in text:
      if t in coder:
        new_text += coder[t]
      else:
        new_text += t
    return new_text

# ----------------------
# Test for apply_coder()
# ----------------------

# print apply_coder("Hello, world!", build_coder(3))
# print apply_coder("Khoor,czruog!", build_decoder(3))

# ----------------------

def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet,
    so spaces should be replaced by a lowercase letter as appropriate.
    Otherwise, lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text
    returns: text after being shifted by specified amount.

    Example:
    >>> apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    """
    coder = build_coder(shift)
    return apply_coder(text, coder)

def apply_shift_back(text, shift):

    decoder = build_decoder(shift)
    return apply_coder(text, decoder)

# ----------------------
# Test for apply_shift()
# ----------------------

# print apply_shift('This is a test.', 8)

# ----------------------

#
# Problem 2: Codebreaking.
#

def find_best_shift(wordlist, text):
    """
    Decrypts the encoded text and returns the plaintext.

    text: string
    returns: 0 <= int 27

    Example:
    >>> s = apply_coder('Hello, world!', build_encoder(8))
    >>> s
    'Pmttw,hdwztl!'
    >>> find_best_shift(wordlist, s) returns
    8
    >>> apply_coder(s, build_decoder(8)) returns
    'Hello, world!'
    """

    # ------------------------------------------------------
    # This was my original attempt-- it found the first shift that
    # contained all real words, but didn't count the max number
    # and didn't use is_word(), and needed an additional helper
    # function to strip punctuation and build a list.
    # This fucked up later on multi-level decryption,
    # and broke decryption of 3 random word by being ambiguous.
    # ------------------------------------------------------

    # e_words = e_word_list(text)
    # count = 0
    # # print e_words, count
    #
    # while set(e_words).issubset(set(wordlist)) == False:
    #   count += 1
    #   text = apply_shift(text, 1)
    #   e_words = e_word_list(text)
    #   # print e_words, count
    # return count

    # ------------------------------------------------------
    # Below was written using the provided pesudo-code solution.
    # Took about 3 min to implement. Works a dream.
    # ------------------------------------------------------

    best_shift = 0
    valid_words = 0
    max_words = 0


    for n in range(27):
      new_text = apply_shift(text, n)
      list_words = new_text.split()
      for l in list_words:
        if is_word(wordlist, l):
          valid_words += 1
      if valid_words > max_words:
        max_words = valid_words
        best_shift = n
      # print new_text
    return best_shift

# ----------------------
# Test for find_best_shift()
# ----------------------

# s = apply_shift('Hello, world!', 12)
# print find_best_shift(wordlist, s)

# ----------------------


# ------------------------------------------------------
#  DO NOT USE
# ------------------------------------------------------

# def e_word_list(text):
#   '''
#   Helper function that takes a string of text, breaks it into a list of words,
#   and strips the words of any punctuation.
#
#   This is used to generate the list of words to check as valid from the word list.
#   (instead of using the class-provided is_word() function)
#   '''
#
#   words = text.split()
#   for n in range(len(words)):
#     words[n] = words[n].lower()
#     words[n] = words[n].strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
#   return words



#
# Problem 3: Multi-level encryption.
#
def apply_shifts(text, shifts):
    """
    Applies a sequence of shifts to an input text.

    text: A string to apply the Ceasar shifts to
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.
    returns: text after applying the shifts to the appropriate
    positions

    Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    """


    for n in range(len(shifts)):
      shifted_text = apply_shift(text[shifts[n][0]:],shifts[n][1])
      text = text[:shifts[n][0]] + shifted_text
      # print shifted_text, shifts[n][1]
      # print text
      # print
    return text

# ----------------------
# Test for apply_shifts()
# ----------------------

# s = "Do Androids Dream of Electric Sheep?"
# print apply_shifts(s, [(0,6), (3, 18), (12, 16)])
# Expected: 'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'

# s = 'tjxuojyfJxkgsfulfKrkizxoifYnkkv?'
# print
# print apply_shift(s, 18)

# ----------------------



#
# Problem 4: Multi-level decryption.
#


def find_best_shifts(wordlist, text):
    """
    Given a scrambled string, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)

    wordlist: list of words
    text: scambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)

    Examples:
    >>> s = random_scrambled(wordlist, 3)
    >>> s
    'eqorqukvqtbmultiform wyy ion'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> shifts
    [(0, 25), (11, 2), (21, 5)]
    >>> apply_shifts(s, shifts)
    'compositor multiform accents'
    >>> s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    >>> s
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?
    """


# s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
# best_shifts = find_best_shifts(wordlist, s)
# print best_shifts
# print apply_shifts(s, best_shifts)
#
# s = random_scrambled(wordlist, 3)
# shifts = find_best_shifts(wordlist, s)
# print
# print "Encoded string: ", s
# print "Best shifts:" , shifts
# print "Decoded string: ", apply_shifts(s, shifts)




def find_best_shifts_rec(wordlist, text, start):
    """
    Given a scrambled string and a starting position from which
    to decode, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: You will find this function much easier to implement
    if you use recursion.

    wordlist: list of words
    text: scambled text to try to find the words for
    start: where to start looking at shifts
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    """



def decrypt_fable():
     """
    Using the methods you created in this problem set,
    decrypt the fable given by the function get_fable_string().
    Once you decrypt the message, be sure to include as a comment
    at the end of this problem set how the fable relates to your
    education at MIT.

    returns: string - fable in plain text
    """
    ### TODO.




#What is the moral of the story?
#
#
#
#
#
