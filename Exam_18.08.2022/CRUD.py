matrix = []

for _ in range(6):
    matrix.append(list(input().split()))

hero = [int(x) for x in input() if x.isdigit()]

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while True:
    command_args = input().split(", ")
    command = command_args[0]

    if command == "Stop":
        break

    direction = command_args[1]
    hero = [hero[0] + directions[direction][0], hero[1] + directions[direction][1]]

    if command == "Create":
        value = command_args[2]

        if matrix[hero[0]][hero[1]] == ".":
            matrix[hero[0]][hero[1]] = value

    elif command == "Update":
        value = command_args[2]

        if matrix[hero[0]][hero[1]] != ".":
            matrix[hero[0]][hero[1]] = value

    elif command == "Delete":

        if matrix[hero[0]][hero[1]] != ".":
            matrix[hero[0]][hero[1]] = "."

    else:

        if matrix[hero[0]][hero[1]] != ".":
            print(matrix[hero[0]][hero[1]])

for line in matrix:
    print(*line, sep=" ")