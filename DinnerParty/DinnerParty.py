import random
print("Enter the number of friends joining (including you): ")
count = int(input("• "))
if count > 0:
    print("Enter names: ")
    names = {input("• ") for i in range(count)}
    print("Enter the total amount: ")
    amount = int(input("• "))
    value = round(amount / count, 2)
    names = dict.fromkeys(names, value)
    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    action = input("• ")
    lucky = random.choice(list(names.keys()))
    if action == "Yes":
        print(f"{lucky} is the lucky one!")
        names = dict.fromkeys(names, round(amount / (count - 1), 2))
        names[lucky] = 0
    elif action == "No":
        print("No one is going to be lucky")
    print("\n", names)
else:
    print("No one is joining for the party")