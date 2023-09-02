def check_next_position(row: object, col: object, command: object) -> object:
    if command == "U":
        return row - 1, col
    elif command == "D":
        return row + 1,col
    elif command == "L":
        return row, col - 1
    elif command == "R":
        return row, col + 1


def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(x) for x in input().split()]

lair = []
B_location = []
start_row = 0
start_col = 0

for idx1 in range(rows):
    current_row = list(input())
    for idx in range(len(current_row)):
        if current_row[idx] == "P":
            start_row = idx1
            start_col = idx
        elif current_row[idx] == "B":
            B_location.append(list([idx1, idx]))
    lair.append(current_row)

commands = input()
won = False
dead = False

lair[start_row][start_col] = "."

for command in commands:
    next_row, next_col = check_next_position(start_row, start_col, command)

    if is_outside(next_row, next_col, rows, cols):
        lair[start_row][start_col] = "."
        won = True
    else:
        if lair[next_row][next_col] == "B":
            start_row, start_col = next_row, next_col
            dead = True
        else:
            start_row, start_col = next_row, next_col

    new_bunnies = []
    for bunny in B_location:
        bunny_row, bunny_col = bunny[0], bunny[1]

        if not is_outside(bunny_row - 1, bunny_col, rows, cols):
            lair[bunny_row - 1][bunny_col] = "B"
            new_bunnies.append([bunny_row - 1, bunny_col])
        if not is_outside(bunny_row + 1, bunny_col, rows, cols):
            lair[bunny_row + 1][bunny_col] = "B"
            new_bunnies.append([bunny_row + 1, bunny_col, rows, cols])
        if not is_outside(bunny_row, bunny_col - 1, rows, cols):
            lair[bunny_row][bunny_col - 1] = "B"
            new_bunnies.append([bunny_row, bunny_col - 1])
        if not is_outside(bunny_row, bunny_col + 1, rows, cols):
            lair[bunny_row][bunny_col + 1] = "B"
            new_bunnies.append([bunny_row, bunny_col + 1])

    if lair[start_row][start_col] == "B":
        dead = True

    B_location.extend(new_bunnies)

    if won or dead:
        break

for el in lair:
    print(*el, sep="")

if won:
    print(f"won: {start_row} {start_col}")
else:
    print(f"dead: {start_row} {start_col}")

    ### Second_soliution

from collections import deque

rows, cols = map(int, input().split())

matrix = []
player = []
bunnies_position = []
won = False
dead = False

for row in range(rows):
    line = list(input())
    matrix.append(line)
    for col in range(len(line)):
        if line[col] == "P":
            player = [row, col]
            matrix[row][col] = "."
        elif line[col] == "B":
            bunnies_position.append((row, col))

commands = deque(list(input()))

directions = {
    "U": [-1, 0],
    "D": [1, 0],
    "L": [0, -1],
    "R": [0, 1]
}

while True:
    command = commands.popleft()

    next_position = [player[0] + directions[command][0], player[1] + directions[command][1]]

    if 0 > next_position[0] or 0 > next_position[1] \
        or next_position[0] >= rows or next_position[1] >= cols:
        won = True

    else:
        if matrix[next_position[0]][next_position[1]] == "B":
            dead = True
            player = [next_position[0], next_position[1]]
        else:
            player = [next_position[0], next_position[1]]

    new_bunnies = []
    for b in bunnies_position:
        if b[0] > 0:
            if matrix[b[0] - 1][b[1]] == ".":
                matrix[b[0] - 1][b[1]] = "B"
                new_bunnies.append((b[0] - 1, b[1]))

        if b[0] < rows - 1:
            if matrix[b[0] + 1][b[1]] == ".":
                matrix[b[0] + 1][b[1]] = "B"
                new_bunnies.append((b[0] + 1, b[1]))

        if b[1] > 0:
            if matrix[b[0]][b[1] - 1] == ".":
                matrix[b[0]][b[1] - 1] = "B"
                new_bunnies.append((b[0], b[1] - 1))

        if b[1] < cols - 1:
            if matrix[b[0]][b[1] + 1] == ".":
                matrix[b[0]][b[1] + 1] = "B"
                new_bunnies.append((b[0], b[1] + 1))

    if matrix[player[0]][player[1]] == "B":
        dead = True

    bunnies_position.extend(new_bunnies)

    if won or dead:
        break

[print(''.join(row), sep="\n")for row in matrix]
if won:
    print(f"won: {player[0]} {player[1]}")
elif dead:
    print(f"dead: {player[0]} {player[1]}")


