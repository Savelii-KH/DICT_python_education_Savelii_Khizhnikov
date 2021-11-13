xo_list = input("Enter cells: ")
ceil1 = xo_list[0:3]
ceil2 = xo_list[3:6]
ceil3 = xo_list[6:9]
o_list = ceil1.count("O") + ceil2.count("O") + ceil3.count("O")
x_list = ceil1.count("X") + ceil2.count("X") + ceil3.count("X")
wins = 0


def pole():
    global ceil1, ceil2, ceil3
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


pole()


def wins_count():
    global wins
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


def winner():
    if ceil1[0] == ceil1[1] == ceil1[2] != "_":
        print(str(ceil1[0]) + " won!")
    if ceil1[0] == ceil2[0] == ceil3[0] != "_":
        print(str(ceil1[0]) + " won!")
    if ceil1[0] == ceil2[1] == ceil3[2] != "_":
        print(str(ceil1[0]) + " won!")
    if ceil2[0] == ceil2[1] == ceil2[2] != "_":
        print(str(ceil2[0]) + " won!")
    if ceil3[0] == ceil2[1] == ceil1[2] != "_":
        print(str(ceil3[0]) + " won!")
    if ceil1[1] == ceil2[1] == ceil3[1] != "_":
        print(str(ceil1[1]) + " won!")
    if ceil1[2] == ceil2[2] == ceil3[2] != "_":
        print(str(ceil1[2]) + " won!")


if "_" not in xo_list:
    wins_count()
if "_" in xo_list:
    print("Game not finished!")
if wins > 1:
    print("Impossible")
if wins == 0 and "_" not in xo_list:
    print("Draw")
if wins == 1:
    if x_list - o_list == -(o_list - x_list):
        winner()
