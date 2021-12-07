import random
value = 0


def addiction():
    while True:
        for_start_list = input("• ")
        first_list = str(for_start_list).split(",")
        second_list = []
        if len(first_list) == 0:
            return {"rock": "paper", "scissors": "rock", "paper": "scissors"}
        elif len(first_list) % 2 == 0:
            print("Enter an unpaired number of elements")
        elif int(len(first_list)) > 0:
            if len(first_list) % 2 != 0:
                for i in range(len(first_list)):
                    zav = []
                    for j in range(int(len(first_list)/2)):
                        zav.append(first_list[i-(j+1)])
                    second_list.append(zav)
                return {first_list[i]: second_list[i] for i in range(len(first_list))}


while True:
    start = input("Start the game (y/n): ")
    if start == "y":
        name = input("Enter your name: ")
        print(f"Hello {name} \n")
        print("Enter game elements: ")
        elements = addiction()
        with open("rating.txt", "r") as f:
            lines = f.readline()
            lines = str(lines).split()
            line = {lines[i]: int(lines[i + 1]) for i in range(0, len(lines), 2)}
            if name in line.keys():
                value = line[name]
            print("\nEnter your choice:")
        while True:
            comp = random.choice(list(elements.keys()))
            player = input("• ")
            if player in elements:
                if player in comp:
                    value += 50
                    print(f"There is a draw {comp}")
                elif comp in elements[player]:
                    value += 100
                    print(f"Well done. The computer chose {comp} and failed")
                elif player in elements[comp]:
                    print(f"Sorry, but the computer chose {comp}")
            elif player == "!rating":
                print(f"Your rating: {value}")
            elif player == "!exit":
                print(f"Bye {name}!\n")
                break
            elif player not in elements.keys() and player != "!exit" and player != "!rating":
                print("Invalid input")
    elif start == "n":
        print("Bye!")
        break
    else:
        print("Invalid input")
