rows = int(input())

matrix = []

for i in range(rows):
    matrix.extend([int(x) for x in input().split(", ")])

print(matrix)