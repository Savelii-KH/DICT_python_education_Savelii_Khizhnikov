import random

code_words = ["python", "java", "javascript", "php"]
word_number = random.randint(0, 3)
word = list(code_words[word_number])
length = len(word)
replaced_word = ["-" for letter in word]
print("""       HANGMAN         
If you want play print "Start", else you exit from game
""")
joined_word = ("".join(word))
x = 8

start = input()
if start == "Start":
    while x > 0:
        print("".join(replaced_word))
        print("Your tries: " + str(x))
        letter = str(input("Input a letter: ").strip(""))
        if letter in word:
            for i, c in enumerate(word):
                if letter == c:
                    replaced_word[i] = letter
            if "-" not in replaced_word:
                print("Your word is: '" + str("".join(replaced_word)) + "', and you won!")
                break
        else:
            x -= 1
    if x == 0:
        print("You lost")

