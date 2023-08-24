rows, cols = [int(i) for i in input().split(", ")]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

total = 0

for row in matrix:
    for num in row:
        total += num

print(total)
print(matrix)

