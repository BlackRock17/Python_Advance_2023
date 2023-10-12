size = int(input())
reg = input()
car_pos = [0, 0]
tunnel = []
matrix = []
km = 0

for row in range(size):
    line = list(input().split())
    matrix.append(line)

    for col in range(len(line)):
        if line[col] == "T":
            tunnel.append([row, col])

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while True:
    command = input()
    if command == "End":
        print(f"Racing car {reg} DNF.")
        print(f"Distance covered {km} km.")
        break

    r, c = car_pos[0] + directions[command][0], car_pos[1] + directions[command][1]

    if matrix[r][c] == ".":
        car_pos = [r, c]
        km += 10

    elif matrix[r][c] == "T":
        if r == tunnel[0][0] and c == tunnel[0][1]:
            car_pos = [tunnel[1][0], tunnel[1][1]]
        else:
            car_pos = [tunnel[0][0], tunnel[0][1]]

        matrix[tunnel[0][0]][tunnel[0][1]] = "."
        matrix[tunnel[1][0]][tunnel[1][1]] = "."
        km += 30

    else:
        car_pos = [r, c]
        km += 10
        print(f"Racing car {reg} finished the stage!")
        print(f"Distance covered {km} km.")
        break

matrix[car_pos[0]][car_pos[1]] = "C"

for line in matrix:
    print(''.join(line))
