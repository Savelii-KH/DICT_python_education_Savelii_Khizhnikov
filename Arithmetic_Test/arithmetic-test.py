import random

answer = None
level = None
score = 0
l1 = "Simple arithmetic operations with numbers from 2 to 9"
l2 = "Squaring numbers from 11 to 29"
l3 = "Raising to the third power of a number from 2 to 10"
levels = [l1, l2, l3]
scores = []
completed_levels = []


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


def level_3():
    global answer, score
    x = 0
    while x < 5:
        a = random.randint(2, 10)
        answer = a ** 3
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
    print(f"Your mark is {score}/5")
    return score


def score_saving():
    global level, scores, completed_levels
    while True:
        print("\nWould you like to save your result to the file? For save print - 1, without saving  - 0.")
        try:
            action = int(input("• "))
            if action == 1:
                print("Enter your name:")
                name = input("• ")
                r = [f"{levels[i]}: {scores[i]}/5" for i in range(len(completed_levels))]
                result = "\n".join(r)
                try:
                    with open("result.txt", "a") as f:
                        f.write(f"""{"-" *  (49 - int(len(name)))} {name} {"-" * 49}
{result}
{"-" * 100}\n""")
                        print("The results are saved in ""results.txt"" \n")
                        break
                except FileNotFoundError:
                    with open("result.txt", "w") as f:
                        f.write(f"""{"-" * (49 - int(len(name)))} {name} {"-" * 49}
{result}
{"-" * 100}\n""")
                        print("The results are saved in ""results.txt"" \n")
                        break
            elif action == 0:
                break
            else:
                print("Choose one of the options")
        except ValueError:
            print("Incorrect format")


while True:
    try:
        print(f"""{"-" * 64}
This is simple arithmetic test with three levels of difficulty.
For starting test print - 1, for exit - 0.
Good luck)\n{"-" * 64}\n""")
        print("Enter your choice:")
        choice = int(input("• "))
        if choice == 1:
            print(f"\nLevel 1:\n{l1}")
            level_1()
            if score >= 4:
                level = 1
                completed_levels.append(level)
                scores.append(score)
                score = 0
                print(f"\nLevel 2:\n{l2}")
                level_2()
                if score >= 4:
                    level = 2
                    completed_levels.append(level)
                    scores.append(score)
                    score = 0
                    print(f"\nLevel 3:\n{l3}")
                    level_3()
                    if score >= 4:
                        level = 3
                        completed_levels.append(level)
                        scores.append(score)
                        score_saving()
                    elif score < 4:
                        level = 3
                        completed_levels.append(level)
                        scores.append(score)
                        score_saving()
                elif score < 4:
                    level = 2
                    completed_levels.append(level)
                    scores.append(score)
                    score_saving()
            elif score < 4:
                completed_levels.append(level)
                scores.append(score)
                level = 1
                print("Bad result\n")
        elif choice == 0:
            break
        else:
            print("Incorrect choice! Try again")
    except ValueError:
        print("Incorrect format")
