import random

sl = ["+", "-", "*"]
x = 0
n = 0
answer = None

while x < 5:
    a = random.randint(2, 9)
    b = random.randint(2, 9)
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
            action = int(input("> "))
            if action == answer:
                print("Right")
                n += 1
                break
            else:
                print("Wrong")
                break
        except ValueError:
            print("Incorrect format")
    x += 1
print(f"You mark is {n}/5.")
