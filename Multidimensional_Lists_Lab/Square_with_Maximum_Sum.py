rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

first_row = [0, 0]
second_row = [0, 0]
total = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]

        if current_sum > total:
            first_row[0] = matrix[row][col]
            first_row[1] = matrix[row][col + 1]
            second_row[0] = matrix[row + 1][col]
            second_row[1] = matrix[row + 1][col + 1]
            total = current_sum

print(*first_row)
print(*second_row)
print(total)

