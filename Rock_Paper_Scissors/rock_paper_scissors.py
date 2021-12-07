import random
elements = {"paper": "rock", "rock": "scissors", "scissors": "paper"}
while True:
    comp = random.choice(list(elements.values()))
    player = input("• ")
    if player in elements.keys():
        if player == comp:
            print(f"There is a draw {comp}")
        if player == elements[comp]:
            print(f"Sorry, but the computer chose {comp}")
        if comp == elements[player]:
            print(f"Well done. The computer chose {comp} and failed")
    elif player == "!exit":
        print("Bye!")
        break
    else:
        print("Invalid input")
