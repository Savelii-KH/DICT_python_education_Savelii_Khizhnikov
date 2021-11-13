import random
xo_list = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
ceil1 = xo_list[0:3]
ceil2 = xo_list[3:6]
ceil3 = xo_list[6:9]
o_list = ceil1.count("O") + ceil2.count("O") + ceil3.count("O")
x_list = ceil1.count("X") + ceil2.count("X") + ceil3.count("X")
xo_number = random.randint(0, 1)
x_or_o = ("X", "O")
xo = x_or_o[xo_number]
wins = 0


def xo_placed():
    global xo
    if xo == "X":
        xo = "O"
    else:
        xo = "X"


def pole():
    global ceil1, ceil2, ceil3
    print("----------")
    print("|", end=" ")
    for a in ceil1:
        print(a, end=" ")
    print("|")
    print("|", end=" ")
    for b in ceil2:
        print(b, end=" ")
    print("|")
    print("|", end=" ")
    for c in ceil3:
        print(c, end=" ")
    print("|")
    print("----------")


pole()


while True:
    inp = input("Write coordinate(yx): ")
    list_inp = list(inp)
    joined_inp = "".join(list_inp)
    if int(joined_inp[:1]) >= 1 or int(joined_inp[:1]) <= 3:
        if int(joined_inp[2:3]) >= 1 or int(joined_inp[2:3]) <= 3:
            if joined_inp[:1] == "1":
                if joined_inp[2:3] == "1":
                    if ceil1[0] != "X" and ceil1[0] != "O":
                        ceil1[0] = xo
                        xo_placed()
                    else:
                        print("This cell is occupied! Choose another one!")
                if joined_inp[2:3] == "2":
                    if ceil1[1] != "X" and ceil1[1] != "O":
                        ceil1[1] = xo
                        xo_placed()
                    else:
                        print("This cell is occupied! Choose another one!")
                if joined_inp[2:3] == "3":
                    if ceil1[2] != "X" and ceil1[2] != "O":
                        ceil1[2] = xo
                        xo_placed()
                    else:
                        print("This cell is occupied! Choose another one!")
            pole()

    if int(joined_inp[:1]) < 1 or int(joined_inp[:1]) > 3:
        print("Y must be between 1 and 3!")
    if int(joined_inp[2:3]) < 1 or int(joined_inp[2:3]) > 3:
        print("X must be between 1 and 3!")

    if joined_inp[:1] == "2":
        if joined_inp[2:3] == "1":
            if ceil2[0] != "X" and ceil2[0] != "O":
                ceil2[0] = xo
            else:
                print(f"This cell is occupied! Choose another one!")
        if joined_inp[2:3] == "2":
            if ceil2[1] != "X" and ceil2[1] != "O":
                ceil2[1] = xo
            else:
                print("This cell is occupied! Choose another one!")
        if joined_inp[2:3] == "3":
            if ceil2[2] != "X" and ceil2[2] != "O":
                ceil2[2] = xo
            else:
                print("This cell is occupied! Choose another one!")

    if joined_inp[:1] == "3":
        if joined_inp[2:3] == "1":
            if ceil3[0] != "X" and ceil3[0] != "O":
                ceil3[0] = xo
            else:
                print("This cell is occupied! Choose another one!")
        if joined_inp[2:3] == "2":
            if ceil3[1] != "X" and ceil3[1] != "O":
                ceil3[1] = xo
            else:
                print("This cell is occupied! Choose another one!")
        if joined_inp[2:3] == "3":
            if ceil3[2] != "X" and ceil3[2] != "O":
                ceil3[2] = xo
            else:
                print("This cell is occupied! Choose another one!")

    if ceil1[0] == ceil1[1] == ceil1[2] != "_":
        wins += 1
    if ceil1[0] == ceil2[0] == ceil3[0] != "_":
        wins += 1
    if ceil1[0] == ceil2[1] == ceil3[2] != "_":
        wins += 1
    if ceil2[0] == ceil2[1] == ceil2[2] != "_":
        wins += 1
    if ceil3[0] == ceil3[1] == ceil3[2] != "_":
        wins += 1
    if ceil3[0] == ceil2[1] == ceil1[2] != "_":
        wins += 1
    if ceil1[1] == ceil2[1] == ceil3[1] != "_":
        wins += 1
    if ceil1[2] == ceil2[2] == ceil3[2] != "_":
        wins += 1

    if wins == 1:
        if x_list - o_list == -(o_list - x_list):
            if ceil1[0] == ceil1[1] == ceil1[2] != "_":
                print(str(ceil1[0]) + " won!")
                break
            if ceil1[0] == ceil2[0] == ceil3[0] != "_":
                print(str(ceil1[0]) + " won!")
                break
            if ceil1[0] == ceil2[1] == ceil3[2] != "_":
                print(str(ceil1[0]) + " won!")
                break
            if ceil2[0] == ceil2[1] == ceil2[2] != "_":
                print(str(ceil2[0]) + " won!")
                break
            if ceil3[0] == ceil2[1] == ceil1[2] != "_":
                print(str(ceil3[0]) + " won!")
                break
            if ceil1[1] == ceil2[1] == ceil3[1] != "_":
                print(str(ceil1[1]) + " won!")
                break
            if ceil1[2] == ceil2[2] == ceil3[2] != "_":
                print(str(ceil1[2]) + " won!")
                break
        else:
            print("Impossible")
            break
    elif wins == 0 and "_" not in xo_list[0:8]:
        print("Draw")
        break
