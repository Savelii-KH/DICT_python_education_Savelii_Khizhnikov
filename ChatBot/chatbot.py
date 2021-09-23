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
