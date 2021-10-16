import random

print("                             HANGMAN")


def start_game():
    start = input("If you want play print \"Start\", else if you want exit print \"Exit\": ")
    if start == "Start" or start == "start":
        print("\nThe game started!")
        game()
    elif start == "Exit" or start == "exit":
        print("You will exit")


def game():
    code_words = ["python", "java", "javascript", "php"]
    word_number = random.randint(0, 3)
    word = list(code_words[word_number])
    length = len(word)
    replaced_word = ["-" for letter in word]
    joined_word = ("".join(word))
    x = 8

    while True:
        print("\n" + "".join(replaced_word))
        letter = str(input("Input a letter: ").strip(""))
        letter_len = len(letter)
        if letter.isalpha():
            if letter.islower():
                if letter_len == 1:
                    if letter in word:
                        for i, c in enumerate(word):
                            if letter in replaced_word[i]:
                                x -= 1
                                print("You\'ve already guessed this letter")
                                continue
                            if letter == c:
                                replaced_word[i] = letter
                    else:
                        x -= 1
                        print("That's letter doesn't appear in the word")
                else:
                    print("You should input a single letter")
            else:
                print("Please, input a lowercase English letter")
        else:
            print("Please, input a English letter")
        if "-" not in replaced_word:
            print("Your word is: '" + str("".join(replaced_word)) + "', and you won!")
            start_game()
            return
    if x <= 0:
        print("You lost!")
        return

start_game()
