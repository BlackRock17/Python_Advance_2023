from collections import deque

field_size = int(input())
commands = deque(input().split(", "))

field = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

squirrel = []

hazelnuts = 0

for row in range(field_size):
    line = input()
    field.append(list(line))

    if "s" in line:
        squirrel = [row, line.index("s")]

while commands:
    command = commands.popleft()
    next_move = [squirrel[0] + directions[command][0], squirrel[1] + directions[command][1]]

    if not (0 <= next_move[0] < field_size and 0 <= next_move[1] < field_size):
        print("The squirrel is out of the field.")
        break

    elif field[next_move[0]][next_move[1]] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    elif field[next_move[0]][next_move[1]] == "h":
        hazelnuts += 1
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break

    elif len(commands) == 0:
        print("There are more hazelnuts to collect.")
        break

    field[squirrel[0]][squirrel[1]] = "*"
    squirrel = [next_move[0], next_move[1]]

print(f"Hazelnuts collected: {hazelnuts}")




