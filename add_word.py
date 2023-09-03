#!/usr/bin/env python3

def main():
  new_word = str(input("Enter the new word you would like to add: "))
  with open("words.py", "r") as f:
    words = f.readlines()
    words = words[0][9:]
#    f.close()
#  words.append(new_word)
#  with open("words.py", "w") as w:
#    w.write("words = "+ str(words))
  print("Added!")

if __name__ == "__main__":
  main()

