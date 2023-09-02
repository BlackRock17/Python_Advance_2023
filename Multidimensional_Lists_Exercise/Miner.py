from collections import deque

def check_position():
    if 0 <= next_position[0] < size and 0 <= next_position[1] < size:
        return True
    return False


size = int(input())

commands = deque(input().split())

matrix = []
coal = 0
miner = []
game_over = False

for row in range(size):
    line = input().split()
    matrix.append(line)
    for col in range(len(line)):
        if line[col] == "s":
            miner = [row, col]
            matrix[row][col] = "*"
        elif line[col] == "c":
            coal += 1

directions = {
    "up": [-1, 0],
    "down": [+1, 0],
    "left": [0, -1],
    "right": [0, +1]
}

while commands:
    command = commands.popleft()

    next_position = [miner[0] + directions[command][0], miner[1] + directions[command][1]]

    if not check_position():
        continue

    miner = [next_position[0], next_position[1]]

    if matrix[next_position[0]][next_position[1]] == "*":
        continue

    elif matrix[next_position[0]][next_position[1]] == "c":
        coal -= 1
        matrix[next_position[0]][next_position[1]] = "*"
        if coal == 0:
            break

    elif matrix[next_position[0]][next_position[1]] == "e":
        game_over = True
        break

if game_over:
    print(f"Game over! ({miner[0]}, {miner[1]})")
elif coal == 0:
    print(f"You collected all coal! ({miner[0]}, {miner[1]})")
else:
    print(f"{coal} pieces of coal left. ({miner[0]}, {miner[1]})")

