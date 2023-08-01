import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabeet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
      print("You have", lives, "lives left,", "letters used:", " ".join(used_letters))
      word_list = [letter if letter in used_letters else "-" for letter in word]
      print("Current word:", " ".join(word_list))
      user_letter = input("Guess a letter: ").upper()
      if user_letter in alphabeet - used_letters:
          used_letters.add(user_letter)
          if user_letter in word_letters:
              word_letters.remove(user_letter)
          else:
              lives = lives - 1
              print("Letter is not in the word")

      elif user_letter in used_letters:
          print("Already guessed that letter")
      else:
          print("Character is invalid")

    if lives == 0:
        print("Game over, the word was:", word)
    else:
        print("You guessed the word:", word)

hangman()
