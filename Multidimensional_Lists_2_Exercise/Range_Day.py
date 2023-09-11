size = 5
matrix = []
hero = []
killed_position = []
targets_left = 0

for row in range(size):
    info = list(input().split())
    matrix.append(info)

    for col in range(len(info)):
        if info[col] == "A":
            hero = [row, col]
            matrix[row][col] = "."
        elif info[col] == "x":
            targets_left += 1

num_commands = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for _ in range(num_commands):
    command_args = input().split()
    command = command_args[0]
    way = command_args[1]

    if command == "shoot":
        next_move = [hero[0] + directions[way][0], hero[1] + directions[way][1]]
        while True:
            if 0 <= next_move[0] < size and 0 <= next_move[1] < size:
                if matrix[next_move[0]][next_move[1]] == "x":
                    matrix[next_move[0]][next_move[1]] = "."
                    targets_left -= 1
                    killed_position.append([next_move[0], next_move[1]])
                    break
                next_move = [next_move[0] + directions[way][0], next_move[1] + directions[way][1]]
            else:
                break

        if targets_left == 0:
            break

    elif command == "move":
        steps = int(command_args[2])

        if way == "up" and 0 <= hero[0] - steps < size and matrix[hero[0] - steps][hero[1]] == ".":
            hero = [hero[0] - steps, hero[1]]

        elif way == "down" and 0 <= hero[0] + steps < size and matrix[hero[0] + steps][hero[1]] == ".":
            hero = [hero[0] + steps, hero[1]]

        elif way == "left" and 0 <= hero[1] - steps < size and matrix[hero[0]][hero[1] - steps] == ".":
            hero = [hero[0], hero[1] - steps]

        elif way == "right" and 0 <= hero[1] + steps < size and matrix[hero[0]][hero[1] + steps] == ".":
            hero = [hero[0], hero[1] + steps]


if targets_left:
    print(f"Training not completed! {targets_left} targets left.")
else:
    print(f"Training completed! All {len(killed_position)} targets hit.")

for el in killed_position:
    print(el)



