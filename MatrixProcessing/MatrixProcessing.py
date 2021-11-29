def input_matrix():
    mat_size = input("Enter size of matrix: ").split()
    mat = []
    print("Enter matrix:")
    for i in range(int(mat_size[0])):
        line = input(int()).split()
        mat.append(line)
        if len(mat[i]) != int(mat_size[1]):
            print("Incorrect size")
            break
    return mat, mat_size,


def summa():
    a, a_size = input_matrix()
    b, b_size = input_matrix()
    print("The result is:")
    if a_size == b_size:
        for i in range(len(a)):
            for j in range(len(a[i])):
                print(int(a[i][j]) + int(b[i][j]), end=" ")
            print(" ")
    if a_size != b_size:
        print("ERROR")


def constant():
    a, a_size = input_matrix()
    const = int(input())
    print("The result is:")
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(int(a[i][j]) * int(const), end=" ")
        print(" ")


def multiply():
    a, a_size = input_matrix()
    b, b_size = input_matrix()
    c = 0

    for i in range(len(a)):
        for j in range(len(a[i])):
            for k in range(len(b)):
                c += int(a[i][k]) * int(b[k][j])
            print(c, end=" ")
            c = 0
        print(" ")


def transpose():
    while True:
        print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        a, a_size = input_matrix()
        action = input("• ")
        if action == "1":
            print("The result is:")
            for i in range(len(a)):
                for j in range(len(a[i])):
                    print(int(a[j][i]), end=" ")
                print(" ")

        elif action == "2":
            print("The result is:")
            for i in range(len(a) - 1, -1, -1):
                for j in range(len(a[i])):
                    print(int(a[-1-j][i]), end=" ")
                print(" ")

        elif action == "3":
            print("The result is:")
            for i in range(len(a)):
                for j in range(len(a[i])):
                    print(int(a[i][-1-j]), end=" ")
                print(" ")

        elif action == "4":
            print("The result is:")
            for i in range(len(a)):
                for j in range(len(a[i])):
                    print(int(a[-1-i][j]), end=" ")
                print(" ")
        break


def minor(mat, i, j):
    return [k[:j] + k[j+1:] for k in (mat[:i]+mat[i+1:])]


def determinant(mat):
    if len(mat) == 2:
        return int(mat[0][0])*int(mat[1][1])-int(mat[0][1])*int(mat[1][0])
    det = 0
    for c in range(len(mat)):
        det += ((-1)**c)*int(mat[0][c])*determinant(minor(mat, 0, c))
    return det


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
0. Exit""")
    choice = input("• ")
    if choice == "1":
        summa()
    elif choice == "2":
        constant()
    elif choice == "3":
        multiply()
    elif choice == "4":
        transpose()
    elif choice == "5":
        mat_a, mat_a_size = input_matrix()
        print("The result is:")
        print(determinant(mat_a))
    elif choice == "0":
        break
    else:
        print("Incorrect parameter")
