rows, cols = [int(x) for x in input().split()]

matrix = []

hero_position = []

for row in range(rows):
    col = input().split()
    matrix.append(list(col))

    if "B" in col:
        hero_position = [row, col.index("B")]

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

moves = 0
touch_opp = 0

while True:
    command = input()

    if command == "Finish":
        break

    next_move = [hero_position[0] + directions[command][0], hero_position[1] + directions[command][1]]

    if next_move[0] < 0 or next_move[0] >= rows or next_move[1] < 0 or next_move[1] >= cols \
            or matrix[next_move[0]][next_move[1]] == "O":
        continue

    if matrix[next_move[0]][next_move[1]] == "-":
        moves += 1
        matrix[hero_position[0]][hero_position[1]] = "-"
        hero_position = [next_move[0], next_move[1]]

    elif matrix[next_move[0]][next_move[1]] == "P":
        moves += 1
        touch_opp += 1
        matrix[hero_position[0]][hero_position[1]] = "-"
        matrix[next_move[0]][next_move[1]] = "-"
        hero_position =[next_move[0], next_move[1]]

    if touch_opp == 3:
        break

print("Game over!")
print(f"Touched opponents: {touch_opp} Moves made: {moves}")
