size = int(input())

matrix = []
marine = []
battle = 0
mines = 0

for row in range(size):
    line = list(input())
    matrix.append(line)

    if "S" in line:
        marine = [row, line.index("S")]
        matrix[marine[0]][marine[1]] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()

    next_position = [marine[0] + directions[command][0], marine[1] + directions[command][1]]

    if matrix[next_position[0]][next_position[1]] == "C":
        battle += 1

    elif matrix[next_position[0]][next_position[1]] == "*":
        mines += 1

    matrix[next_position[0]][next_position[1]] = "-"
    marine = [next_position[0], next_position[1]]

    if battle == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break
    elif mines == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{marine[0]}, {marine[1]}]!")
        break

matrix[marine[0]][marine[1]] = "S"

for l in matrix:
    print(*l, sep="")

