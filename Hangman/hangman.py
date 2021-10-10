import random

words = ("python", "php", "java", "javascript")
word = random.choice(words)

print("HANGMAN")

input_word = input("Guess the word: ")

if input_word == word:
    print("You win!")
else:
    print("You lost!")
