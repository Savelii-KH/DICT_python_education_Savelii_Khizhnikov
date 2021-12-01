print("Enter the number of friends joining (including you): ")
count = int(input("• "))

if count > 0:
    print("Enter names: ")
    names = {input("• "): 0 for i in range(count)}
    print(names)
else:
    print("No one is joining for the party")
