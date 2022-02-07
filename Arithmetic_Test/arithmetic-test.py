import random

answer = None
level = None
score = 0
l1 = "Simple arithmetic operations with numbers from 2 to 9"
l2 = "Squaring numbers from 11 to 29"
levels = [l1, l2]


def level_1():
    global answer, score
    x = 0
    sl = ["+", "-", "*"]
    while x < 5:
        a = random.randint(2, 9)
        b = random.randint(2, 3)
        s = random.randint(0, 2)
        print(f"{a} {sl[s]} {b}")
        if s == 0:
            answer = a + b
        elif s == 1:
            answer = a - b
        else:
            answer = a * b
        while True:
            try:
                action = int(input("• "))
                if action == answer:
                    print("Right")
                    score += 1
                    break
                else:
                    print("Wrong")
                    break
            except ValueError:
                print("Incorrect format")
        x += 1
    print(f"You mark is {score}/5.")
    return score


def level_2():
    global answer, score
    x = 0
    while x < 5:
        a = random.randint(11, 29)
        answer = a ** 2
        print(answer)
        while True:
            try:
                action = int(input("• "))
                if action == a:
                    print("Right")
                    score += 1
                    break
                else:
                    print("Wrong")
                    break
            except ValueError:
                print("Incorrect format")
        x += 1
    print(f"You mark is {score}/5.")
    return score


def score_saving():
    global level, score
    while True:
        print("\nWould you like to save your result to the file? Enter yes or no.")
        action = input("• ")
        if action == "yes" or action == "Yes":
            print("Enter your name:")
            name = input("• ")
            try:
                with open("result.txt", "a") as f:
                    f.write(f"{name}: {score}/5 in level {level} {levels[level-1]}\n")
                    print("The results are saved in ""results.txt""")
                    break
            except FileNotFoundError:
                with open("result.txt", "w") as f:
                    f.write(f"{name}: {score}/5 in level {level} {levels[level-1]}\n")
                    print("The results are saved in ""results.txt""")
                    break
        elif action == "no" or action == "No":
            break
        else:
            print("Choose one of the options")


while True:
    print(f"""\nWhich level do you want to pass:
    #0 Quit the game;
    #1 {l1};
    #2 {l2};""")
    print("="*50)
    choice = input("• ")
    if choice == "1":
        print("\nStart")
        level = 1
        level_1()
        score_saving()
        score = 0
    elif choice == "2":
        print("\nStart")
        level = 2
        level_2()
        score_saving()
        score = 0
    elif choice == "0":
        print("Goodbye")
        break
    else:
        print("The selected level must be between 1 and 2")
