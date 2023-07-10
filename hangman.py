import random
import string
from words import words  # frmo filename, import variable


def get_valid_word(words):
    word = random.choice(words)  # takes list, random chooses from list
    while "-" in word or " " in word:
        word = random.choice(word)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    lives = 6
    # getting user input
    while len(word_letters) > 0 or lives == 0:
      print("you have guessed: ", ' '.join(used_letters))

      # what current word is 
      # it will show the letter if letter is in used letters, otherwise show a hyphen for each letter in word
      word_list = [letter if letter in used_letters else '-' for letter in word]
      print(f"Current word: {' '.join(word_list)}")
      user_input = input("Type in a letter: ").upper()
      if user_input in alphabet - used_letters:
          used_letters.add(user_input)
          if user_input in word_letters:
              word_letters.remove(user_input)
          else:
              lives = lives - 1
              print(f'You have {lives} lives left.')
      elif user_input in used_letters:
          print("You have already used that character. Please try again")
      else:
          print("Invalid character. Please try again")
    if lives == 0:
        print('You died, sorry The word was ', word)
    else:
        print(f"Game over! The word was {word}.")



hangman()
