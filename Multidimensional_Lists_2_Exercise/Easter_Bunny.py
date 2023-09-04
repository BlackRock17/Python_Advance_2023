size = int(input())

matrix = []

bunny_row = 0
bunny_col = 0

for r in range(size):
    line = input().split()
    matrix.append(line)
    for c in range(size):
        if line[c] == "B":
            bunny_row = r
            bunny_col = c

paths = {"up": [], "down": [], "left": [], "right": []}

for direction in paths:
    row = bunny_row
    col = bunny_col
    while True:
        if direction == "up" and 0 < row and matrix[row - 1][col].isdigit():
            paths[direction].append([row - 1, col])
            row -= 1

        elif direction == "down" and size - 1 > row and matrix[row + 1][col].isdigit():
            paths[direction].append([row + 1, col])
            row += 1

        elif direction == "left" and 0 < col and matrix[row][col - 1].isdigit():
            paths[direction].append([row, col - 1])
            col -= 1

        elif direction == "right" and size - 1 > col and matrix[row][col + 1].isdigit():
            paths[direction].append([row, col + 1])
            col += 1

        else:
            break


best_sum = float("-inf")
best_direction = ""
for direc, value in paths.items():
    sum_ = 0
    for el in value:
        sum_ += int(matrix[el[0]][el[1]])
    if sum_ > best_sum and len(value) > 0:
        best_sum = sum_
        best_direction = direc

print(best_direction)

if best_direction:
    for path in paths[best_direction]:
        print(path)

print(best_sum)


######### SECOND SOLUTION

size = int(input())

matrix = []
B_position = []
best_direction = []
best_score = float("-inf")
best_way = ""

for row in range(size):
    data = list(input().split())
    matrix.append(data)

    for col in range(len(data)):
        if data[col] == "B":
            B_position = [row, col]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for way, direction in directions.items():
    score = 0
    current_direction = []
    next_move = [B_position[0] + direction[0], B_position[1] + direction[1]]
    current_position = next_move

    while True:
        if 0 <= current_position[0] < size and 0 <= current_position[1] < size and \
            matrix[current_position[0]][current_position[1]].isdigit():
            score += int(matrix[current_position[0]][current_position[1]])
            current_direction.append([current_position[0], current_position[1]])
            current_position = [current_position[0] + direction[0], current_position[1] + direction[1]]

        else:
            if score > best_score and len(current_direction) > 0:
                best_score = score
                best_direction = current_direction
                best_way = way
            break

print(best_way)
if best_direction:
    for dir in best_direction:
        print(dir)
print(best_score)