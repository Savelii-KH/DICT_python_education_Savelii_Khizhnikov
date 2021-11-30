def input_matrix():
    mat_size = input("Enter size of matrix: ").split()
    mat = []
    print("Enter matrix:")
    for i in range(int(mat_size[0])):
        line = input().split()
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
    print("The result is:")
    for i in range(len(a)):
        for j in range(len(a[i])):
            for k in range(len(b)):
                c += int(a[i][k]) * int(b[k][j])
            print(c, end=" ")
            c = 0
        print(" ")


def transpose_main_d():
    a, a_size = input_matrix()
    print("The result is:")
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(int(a[j][i]), end=" ")
        print(" ")


def transpose_side_d():
    a, a_size = input_matrix()
    print("The result is:")
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(a[i])):
            print(int(a[-1-j][i]), end=" ")
        print(" ")


def transpose_vertical():
    a, a_size = input_matrix()
    print("The result is:")
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(int(a[i][-1-j]), end=" ")
        print(" ")


def transpose_horizontal():
    a, a_size = input_matrix()
    print("The result is:")
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(int(a[-1-i][j]), end=" ")
        print(" ")


def minor(mat, i, j):
    return [k[:j] + k[j+1:] for k in (mat[:i]+mat[i+1:])]


def determinant(mat):
    if len(mat) == 2:
        return int(mat[0][0])*int(mat[1][1])-int(mat[0][1])*int(mat[1][0])
    det = 0
    for c in range(len(mat)):
        det += ((-1)**c)*int(mat[0][c])*determinant(minor(mat, 0, c))
    return det


def inverse_mat():
    a, a_size = input_matrix()
    det_a = determinant(a)
    if det_a != 0:
        print("The result is:")
        if len(a) == 2:
            row_1 = [float(a[1][1])/det_a, -1 * float(a[0][1])/det_a]
            row_2 = [-1 * float(a[1][0])/det_a, float(a[0][0])/det_a]
            return row_1, row_2
        else:
            result_mat = []
            for i in range(len(a)):
                result_mat_rows = []
                for j in range(len(a[i])):
                    m = minor(a, i, j)
                    result_mat_rows.append(((-1) ** (i + j)) * determinant(m))
                result_mat.append(result_mat_rows)
            result_mat = [[result_mat[j][i] for j in range(len(result_mat))] for i in range(len(result_mat[0]))]
            for i in range(len(result_mat)):
                for j in range(len(result_mat)):
                    result_mat[i][j] = result_mat[i][j]/det_a
        for i in range(len(result_mat)):
            for j in result_mat[i]:
                print(round(j, 2), end=" ")
            print(" ")
        return result_mat
    else:
        print("Inverse matrix does not exist")


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6.  Inverse matrix
0. Exit""")
    choice = input("• ")
    if choice == "1":
        summa()
    elif choice == "2":
        constant()
    elif choice == "3":
        multiply()
    elif choice == "4":
        print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        action = input("• ")
        if action == "1":
            transpose_main_d()
        elif action == "2":
            transpose_side_d()
        elif action == "3":
            transpose_vertical()
        elif action == "4":
            transpose_horizontal()
        else:
            print("Incorrect parameter")
    elif choice == "5":
        mat_a, mat_a_size = input_matrix()
        print("The result is:")
        print(determinant(mat_a))
    elif choice == "6":
        inverse_mat()
    elif choice == "0":
        break
    else:
        print("Incorrect parameter")
