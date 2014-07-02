# Problem Set 3b
# Name: CZ
# Collaborators (Discussion): --
# Collaborators (Identical Solution): --
# Time: 1:00 (Wednesday)
# Notes: Felt pretty straightforward after figuring out most of it last night.



from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#



def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    score = 0
    answer = ''
    all_perms = []
    valid_words = []
    for n in range(HAND_SIZE + 1):
      all_perms += (get_perms(hand, n))
    valid_words = set(all_perms).intersection(word_list)
    for word in valid_words:
      if get_word_score(word, HAND_SIZE) > score:
          score = get_word_score(word, HAND_SIZE)
          answer = word
    return answer




#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed,
       the remaining letters in the hand are displayed, and the computer
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...
    running_hand = hand.copy()
    running_score = 0
    word = ""
    while sum(running_hand.values()) > 0:
      print "The computer's hand is: ", display_hand(running_hand)
      word = comp_choose_word(running_hand, word_list)
      if get_word_score(word, HAND_SIZE) == 0:
        print "There are no more words to make."
        break
      running_score += get_word_score(word, HAND_SIZE)
      print "Nice!", word, "is worth", get_word_score(word, HAND_SIZE), "points!"
      print
      running_hand = update_hand(running_hand, word)
    print "The computer is done. It scored a total of:", running_score, "points."
    return ""

#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    next = ''
    count = 0
    while next != 'e':
      player = ''
      initialize(count)
      next = raw_input("Enter your choice: ")
      while next not in ('n', 'e') and (count == 0 or next != 'r'):
        print "That is not a valid input. Please try again."
        next = raw_input("Enter your choice: ")
        print
      if next == 'n':
        hand = deal_hand(HAND_SIZE)
        while player not in ('u', 'c'):
          player = comp_or_user()
          print
        if player == 'u':
          play_hand(hand, word_list)
        if player == 'c':
          comp_play_hand(hand, word_list)
        print
        count += 1
      elif next == 'r':
        while player not in ('u', 'c'):
          player = comp_or_user()
          print
        if player == 'u':
          play_hand(hand, word_list)
        if player == 'c':
          comp_play_hand(hand, word_list)
          print
      elif next == 'e':
        return

def comp_or_user():
  print "To play the hand yourself, press 'u'"
  print "To have the computer play, press 'c'"
  player = raw_input("Enter your choice: ")
  return player

#
# Build data structures used for entire session and play game
#

HAND_SIZE = 7

if __name__ == '__main__':
    word_list = load_words()
    print
    play_game(word_list)
