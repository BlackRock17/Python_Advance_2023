N = int(input())

matrix = []

for i in range(N):
    matrix.append([int(x) for x in input().split()])

total = 0
for j in range(len(matrix)):
    for k in range(len(matrix[j])):
        if j == k:
            total += matrix[j][k]

print(total)