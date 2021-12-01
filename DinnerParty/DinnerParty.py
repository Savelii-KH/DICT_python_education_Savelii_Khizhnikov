print("Enter the number of friends joining (including you): ")
count = int(input("• "))

if count > 0:
    print("Enter names: ")
    names = {input("• ") for i in range(count)}
    print("Enter the total amount: ")
    amount = int(input())
    names_d = dict.fromkeys(names, round(amount/count, 2))
    print(names_d)
else:
    print("No one is joining for the party")
