rows, cols = map(int, input().split())

matrix = []

for _ in range(rows):
    matrix.append(input().split())

while True:
    command_args = input()

    if command_args == "END":
        break

    command_args = command_args.split()

    if command_args[0] != "swap" or len(command_args) != 5:
        print("Invalid input!")
        continue

    try:
        row1 = int(command_args[1])
        col1 = int(command_args[2])
        row2 = int(command_args[3])
        col2 = int(command_args[4])
    except ValueError:
        print("Invalid input!")
        continue

    if 0 > row1 or row1 > rows - 1 \
            or 0 > row2 or row2 > rows - 1 \
            or 0 > col1 or col1 > cols - 1 \
            or 0 > col2 or col2 > cols - 1:
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for r in matrix:
        print(f"{' '.join(r)}")