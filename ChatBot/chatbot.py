print("""Hello! My name is Hans.
I was created in 2021.
Please, remind me your name.""")

name = str(input())

print("""What a great name you have, """ + name + """!
Enter remainders of diving your age by 3, 5, 7.""")

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

age = (remainder3 * 70 + remainder5 * 21 + remainder7 + 15) % 105
age = str(age)

print("""Your age is """ + age + """, that's good time to start programming!")
Now I will prove to you that I can count to any number you want""")

num = int(input())
x = int()
while x <= num:
    print(x)
    x += 1

print("""
Lets test your programming knowledge
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")


test = 0
while test != 2:
    test = int(input())
    if test == 2:
        print("""Completed, have a nice day!
Congratulations, have a nice day!""")
    else:
        print("Please, try again.")
