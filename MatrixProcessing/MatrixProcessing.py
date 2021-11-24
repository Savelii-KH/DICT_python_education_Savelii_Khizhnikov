mat_size_a = input().split()
mat_a = []
for i in range(int(mat_size_a[0])):
    line = input().split()
    mat_a.append(line)
    if len(mat_a[i]) != int(mat_size_a[1]):
        print("Incorrect size")
        break

const = input()

for i in range(len(mat_a)):
    for j in range(len(mat_a[i])):
        print(int(mat_a[i][j]) * int(const), end=" ")
    print(" ")
