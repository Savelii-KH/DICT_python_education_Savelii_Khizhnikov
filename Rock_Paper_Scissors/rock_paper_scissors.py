import random
value = 0
elements = {"paper": "rock", "rock": "scissors", "scissors": "paper"}

while True:
    start = input("\nStart the game (y/n): ")
    if start == "y":
        name = input("Enter your name: ")
        print(f"Hello {name}")
        with open("rating.txt", "r") as f:
            lines = f.readline()
            lines = str(lines).split()
            line = {lines[i]: int(lines[i + 1]) for i in range(0, len(lines), 2)}
            if name in line.keys():
                value = line[name]
            print("\nGame started!")
            while True:
                comp = random.choice(list(elements.values()))
                player = input("• ")
                if player in elements.keys():
                    if player == comp:
                        value += 50
                        print(f"There is a draw {comp}")
                    if comp == elements[player]:
                        value += 100
                        print(f"Well done. The computer chose {comp} and failed")
                    if player == elements[comp]:
                        print(f"Sorry, but the computer chose {comp}")
                elif player == "!rating":
                    print(f"Your rating: {value}")
                elif player == "!exit":
                    print("Bye!")
                    break
                elif player not in elements.keys() and player != "!exit" and player != "!rating":
                    print("Invalid input")
    elif start == "n":
        print("Bye!")
        break
    else:
        print("Invalid input")
