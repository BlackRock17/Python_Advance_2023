rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

coordinates = input().split()

for el in coordinates:
    row = int(el[0])
    col = int(el[2])

    if matrix[row][col] < 1:
        continue

    if row > 0:
        if matrix[row - 1][col] > 0:
            matrix[row - 1][col] -= matrix[row][col]

        if col > 0:
            if matrix[row - 1][col - 1] > 0:
                matrix[row - 1][col - 1] -= matrix[row][col]

        if col < rows - 1:
            if matrix[row - 1][col + 1] > 0:
                matrix[row - 1][col + 1] -= matrix[row][col]

    if row < rows - 1:
        if matrix[row + 1][col] > 0:
            matrix[row + 1][col] -= matrix[row][col]

        if col > 0:
            if matrix[row + 1][col - 1] > 0:
                matrix[row + 1][col - 1] -= matrix[row][col]

        if col < rows - 1:
            if matrix[row + 1][col + 1] > 0:
                matrix[row + 1][col + 1] -= matrix[row][col]

    if col > 0 and matrix[row][col - 1] > 0:
        matrix[row][col - 1] -= matrix[row][col]

    if col < rows - 1 and matrix[row][col + 1] > 0:
        matrix[row][col + 1] -= matrix[row][col]

    matrix[row][col] = 0

alive_cells = 0
sum_ = 0

for row in matrix:
    for num in row:
        if num > 0:
            alive_cells += 1
            sum_ += num

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_}")
for row in matrix:
    print(' '.join([str(x) for x in row]))