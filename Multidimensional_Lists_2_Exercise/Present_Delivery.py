presents = int(input())
size = int(input())

santa = []
matrix = []
nice_kids = 0
visited_kids = 0

for r in range(size):
    info = list(input().split())
    matrix.append(info)

    for c in range(size):
        if info[c] == "S":
            santa = [r, c]
            matrix[r][c] = "-"

        elif info[c] == "V":
            nice_kids += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()

    if command == "Christmas morning":
        break

    next_position = [santa[0] + directions[command][0], santa[1] + directions[command][1]]

    if 0 <= next_position[0] < size and 0 <= next_position[1] < size:
        santa = next_position

        if matrix[santa[0]][santa[1]] == "V":
            matrix[santa[0]][santa[1]] = "-"
            presents -= 1
            visited_kids += 1

        elif matrix[santa[0]][santa[1]] == "X":
            matrix[santa[0]][santa[1]] = "-"

        elif matrix[santa[0]][santa[1]] == "C":
            matrix[santa[0]][santa[1]] = "-"

            for direction in directions.values():
                if matrix[santa[0] + direction[0]][santa[1] + direction[1]] == "V":
                    matrix[santa[0] + direction[0]][santa[1] + direction[1]] = "-"
                    presents -= 1
                    visited_kids += 1

                elif matrix[santa[0] + direction[0]][santa[1] + direction[1]] == "X":
                    matrix[santa[0] + direction[0]][santa[1] + direction[1]] = "-"
                    presents -= 1

                if presents == 0 or visited_kids == nice_kids:
                    break

        if presents == 0 or visited_kids == nice_kids:
            break

matrix[santa[0]][santa[1]] = "S"

if not presents and visited_kids < nice_kids:
    print("Santa ran out of presents!")

for line in matrix:
    print(*line)

if visited_kids == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - visited_kids} nice kid/s.")






