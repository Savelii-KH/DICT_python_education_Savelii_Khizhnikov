xo_list = input("Enter cells: ")
ceil1 = xo_list[0:3]
ceil2 = xo_list[3:6]
ceil3 = xo_list[6:9]
o_list = ceil1.count("O") + ceil2.count("O") + ceil3.count("O")
x_list = ceil1.count("X") + ceil2.count("X") + ceil3.count("X")


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