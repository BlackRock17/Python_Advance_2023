from collections import deque

player_one = "1"
player_two = "2"

rows, cols = 6, 7

turn = deque([[1, player_one], [2, player_two]])
board = [["0"] * cols for row in range(rows)]

directions = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, -1),
    (1, 1),
    (-1, -1),
    (-1, 1)
)

while True:
    [print(*row) for row in board]
    player_num, player_sym = turn[0]
    player_col = int(input(f"Player {player_num} choose your column:")) - 1

    if 0 >= player_col > 7:
        print(f"select a valid number between 1 and {cols}")
        continue

    row = 0

    if board[row][player_col] != "0":
        print("No empty space on that column")
        continue

    while True:

        if row == rows - 1 or board[row + 1][player_col] != "0":
            board[row][player_col] = player_sym
            break

        row += 1

    for row in range(rows):
        for col in range(cols):
            if board[row][col] != player_sym:
                continue

            for coordinates in directions:
                r, c = row, col

                for i in range(3):
                    r, c = r + coordinates[0], c + coordinates[1]

                    if not (0 <= r < rows and 0 <= c < cols):
                        break

                    if board[r][c] != player_sym:
                        break
                else:
                    [print(*row) for row in board]
                    print(f"Player {player_sym} is winner")
                    raise SystemExit

    turn.append(turn.popleft())

