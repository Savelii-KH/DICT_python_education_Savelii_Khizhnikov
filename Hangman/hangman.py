import random

words = ("python", "pascal", "java", "javascript")
helped_word_list = ("pyt---", "pas---", "jav-", "jav-------")
word_number = random.randint(0, 3)
word = words[word_number]
helped_word = helped_word_list[word_number]
print("HANGMAN")

input_word = input("Guess the word " + helped_word + ": ")

if input_word == word:
    print("You win!")
else:
    print("You lost!")
