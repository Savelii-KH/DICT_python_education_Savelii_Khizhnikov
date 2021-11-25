def summa():
    print("The result is:")
    if mat_size_a == mat_size_b:
        for i in range(len(mat_a)):
            for j in range(len(mat_a[i])):
                print(int(mat_a[i][j]) + int(mat_b[i][j]), end=" ")
            print(" ")
    if mat_size_a != mat_size_b:
        print("ERROR")


def constant():
    print("The result is:")
    for i in range(len(mat_a)):
        for j in range(len(mat_a[i])):
            print(int(mat_a[i][j]) * int(const), end=" ")
        print(" ")


def multi():
    c = 0
    print("The result is:")
    for i in range(len(mat_a)):
        for j in range(len(mat_a[i])):
            for k in range(len(mat_b)):
                    c += int(mat_a[i][k]) * int(mat_b[k][j])
            print(c, end=" ")
            c = 0
        print(" ")


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit""")
    choice = input("• ")
    if choice == "1":
        mat_size_a = input("Enter size of first matrix: ").split()
        mat_a = []
        print("Enter first matrix:")
        for i in range(int(mat_size_a[0])):
            line = input().split()
            mat_a.append(line)
            if len(mat_a[i]) != int(mat_size_a[1]):
                print("Incorrect size")
                break

        mat_size_b = input("Enter size of second matrix: ").split()
        mat_b = []
        print("Enter second matrix:")
        for c in range(int(mat_size_b[0])):
            line = input().split()
            mat_b.append(line)
            if len(mat_b[c]) != int(mat_size_b[1]):
                print("Incorrect size")
                break
        summa()
        print("")

    elif choice == "2":
        mat_size_a = input("Enter size of  matrix: ").split()
        mat_a = []
        print("Enter matrix:")
        for i in range(int(mat_size_a[0])):
            line = input().split()
            mat_a.append(line)
            if len(mat_a[i]) != int(mat_size_a[1]):
                print("Incorrect size")
                break
        const = int(input("Enter constant: "))
        constant()
        print("")

    elif choice == "3":
        mat_size_a = input("Enter size of first matrix: ").split()
        mat_a = []
        print("Enter first matrix:")
        for i in range(int(mat_size_a[0])):
            line = input().split()
            mat_a.append(line)
            if len(mat_a[i]) != int(mat_size_a[1]):
                print("Incorrect size")
                break

        mat_size_b = input("Enter size of second matrix: ").split()
        mat_b = []
        print("Enter second matrix:")
        for c in range(int(mat_size_b[0])):
            line = input().split()
            mat_b.append(line)
            if len(mat_b[c]) != int(mat_size_b[1]):
                print("Incorrect size")
                break
        multi()
        print("")

    if choice == "0":
        break
