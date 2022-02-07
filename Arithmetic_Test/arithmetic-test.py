import random

sl = ["+", "-", "*"]
a = random.randint(2, 9)
b = random.randint(2, 9)
s = random.randint(0, 2)
answer = None
if s == 0:
    answer = a + b
elif s == 1:
    answer = a - b
else:
    answer = a * b
print(f"{a} {sl[s]} {b}")
action = int(input("> "))
if action == answer:
    print("Right!")
else:
    print("Wrong!")
