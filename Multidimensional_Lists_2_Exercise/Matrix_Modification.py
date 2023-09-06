def check_in_out(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    info = input()

    if info == "END":
        break

    command, row, col, value = info.split()
    row = int(row)
    col = int(col)
    value = int(value)

    if check_in_out(row, col, size):
        if command == "Add":
            matrix[row][col] += value

        else:
            matrix[row][col] -= value

    else:
        print("Invalid coordinates")

for el in matrix:
    print(*el)
