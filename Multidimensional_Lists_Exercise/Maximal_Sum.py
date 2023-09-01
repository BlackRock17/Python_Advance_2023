rows, cols = map(int, input().split())

matrix = []
sum_nums = -2000
index = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = 0
        current_sum += matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
            matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
            matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]

        if current_sum > sum_nums:
            sum_nums = current_sum
            index = [row, col]

print(f"Sum = {sum_nums}")
print(f"{matrix[index[0]][index[1]]} {matrix[index[0]][index[1] + 1]} {matrix[index[0]][index[1] + 2]}")
print(f"{matrix[index[0] + 1][index[1]]} {matrix[index[0] + 1][index[1] + 1]} {matrix[index[0] + 1][index[1] + 2]}")
print(f"{matrix[index[0] + 2][index[1]]} {matrix[index[0] + 2][index[1] + 1]} {matrix[index[0] + 2][index[1] + 2]}")