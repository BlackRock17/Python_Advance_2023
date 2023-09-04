size = int(input())

matrix = []
alice_pos = []

for r in range(size):
    current_line = input().split()
    matrix.append(current_line)
    for c in range(size):
        if current_line[c] == "A":
            alice_pos = [r, c]
            matrix[alice_pos[0]][alice_pos[1]] = "*"

tea = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while tea < 10:
    command = input()

    row = alice_pos[0] + directions[command][0]
    col = alice_pos[1] + directions[command][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    symbol = matrix[row][col]
    matrix[row][col] = "*"

    if symbol == "R":
        break

    if symbol.isdigit():
        tea += int(symbol)

    alice_pos = [row, col]

if tea > 9:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(" ".join(x), sep="\n") for x in matrix]


########## SECOND SOLUTION

size = int(input())

matrix = []
Alice = []
tea_bags = 0
win = False

for row in range(size):
    info = list(input().split())
    matrix.append(info)

    for col in range(len(info)):
        if info[col] == "A":
            Alice = [row, col]
            matrix[row][col] = "*"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()

    next_position = [Alice[0] + directions[command][0], Alice[1] + directions[command][1]]

    if 0 <= next_position[0] < size and 0 <= next_position[1] < size:

        if matrix[next_position[0]][next_position[1]].isdigit():
            tea_bags += int(matrix[next_position[0]][next_position[1]])
            matrix[next_position[0]][next_position[1]] = "*"
            if tea_bags >= 10:
                win = True
                break

        elif matrix[next_position[0]][next_position[1]] == "R":
            matrix[next_position[0]][next_position[1]] = "*"
            break

        matrix[next_position[0]][next_position[1]] = "*"
        Alice = next_position

    else:
        break

if win:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for el in matrix:
    print(*el)

