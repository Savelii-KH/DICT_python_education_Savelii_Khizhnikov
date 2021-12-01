print("Enter the number of friends joining (including you): ")
count = int(input("• "))
names = {}

if count > 0:
    print("Enter names: ")
    for i in range(0, count):
        name = input("• ")
        names[name] = 0
    print(names)
else:
    print("No one is joining for the party")
