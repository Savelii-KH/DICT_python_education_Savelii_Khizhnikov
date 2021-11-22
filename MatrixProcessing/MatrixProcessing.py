mat_size_a = input().split()
mat_a =[]
for i in range(int(mat_size_a[0])):
    line = input().split()
    mat_a.append(line)
    if len(mat_a[i]) > int(mat_size_a[1]):
        print("Incorrect size")
        break

mat_size_b = input().split()
mat_b =[]
for c in range(int(mat_size_b[0])):
    line = input().split()
    mat_b.append(line)
    if len(mat_b[c]) > int(mat_size_b[1]):
        print("Incorrect size")
        break

if mat_size_a == mat_size_b:
    for i in range(len(mat_a)):
        for j in range(len(mat_a[i])):
            print(int(mat_a[i][j]) + int(mat_b[i][j]), end=" ")
        print(" ")
