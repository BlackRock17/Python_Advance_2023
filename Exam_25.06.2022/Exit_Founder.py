from collections import deque

players = deque(input().split(", "))
rest = {"Tom": False, "Jerry": False}

matrix = []

for _ in range(6):
    matrix.append(input().split())

while True:
    row, col = map(int, input().strip("()").split(", "))
    player = players[0]

    if rest[player] == True:
        rest[player] = False

    elif matrix[row][col] == "W":
        rest[player] = True
        print(f"{player} hits a wall and needs to rest.")

    elif matrix[row][col] == "E":
        print(f"{player} found the Exit and wins the game!")
        break

    elif matrix[row][col] == "T":
        print(f"{player} is out of the game! The winner is {players[1]}.")
        break

    players.rotate()
