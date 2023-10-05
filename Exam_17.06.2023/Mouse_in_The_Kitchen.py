size_r, size_c = [int(x) for x in input().split(",")]

matrix = []
mouse = []

for r in range(size_r):
    line = list(input())
    matrix.append(line)

    if "M" in line:
        mouse = [r, line.index("M")]
        matrix[mouse[0]][mouse[1]] = "*"

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while True:
    command = input()

    if command == "danger":
        print("Mouse will come back later!")
        break

    row, col = mouse[0] + directions[command][0], mouse[1] + directions[command][1]

    if 0 > row or row >= size_r or 0 > col or col >= size_c:
        print("No more cheese for tonight!")
        break

    elif matrix[row][col] == "*":
        mouse = [row, col]

    elif matrix[row][col] == "@":
        continue

    elif matrix[row][col] == "T":
        mouse = [row, col]
        print("Mouse is trapped!")
        break

    elif matrix[row][col] == "C":
        mouse = [row, col]
        matrix[row][col] = "*"
        win = False

        for line_ in matrix:
            if "C" in line_:
                break
        else:
            print("Happy mouse! All the cheese is eaten, good night!")
            win = True

        if win:
            break

matrix[mouse[0]][mouse[1]] = "M"

for line in matrix:
    print("".join(line))