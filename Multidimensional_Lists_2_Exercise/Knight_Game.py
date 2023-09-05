def out_in(row, col, size):
    return 0 <= row < size and 0 <= col < size


def attack(knight_row, knight_col, matrix):
    counter = 0
    if out_in(knight_row - 2, knight_col - 1, size) and matrix[knight_row - 2][knight_col - 1] == "K":
        counter += 1
    if out_in(knight_row - 2, knight_col + 1, size) and matrix[knight_row - 2][knight_col + 1] == "K":
        counter += 1
    if out_in(knight_row - 1, knight_col - 2, size) and matrix[knight_row - 1][knight_col - 2] == "K":
        counter += 1
    if out_in(knight_row - 1, knight_col + 2, size) and matrix[knight_row - 1][knight_col + 2] == "K":
        counter += 1
    if out_in(knight_row + 1, knight_col - 2, size) and matrix[knight_row + 1][knight_col - 2] == "K":
        counter += 1
    if out_in(knight_row + 1, knight_col + 2, size) and matrix[knight_row + 1][knight_col + 2] == "K":
        counter += 1
    if out_in(knight_row + 2, knight_col - 1, size) and matrix[knight_row + 2][knight_col - 1] == "K":
        counter += 1
    if out_in(knight_row + 2, knight_col + 1, size) and matrix[knight_row + 2][knight_col + 1] == "K":
        counter += 1
    return counter

size = int(input())

matrix = []

for row in range(size):
   matrix.append(list(input()))

removed_knight = 0

while True:
    best_row = 0
    best_col = 0
    best_value = 0

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                value_knight = attack(row, col, matrix)
                if value_knight > best_value:
                    best_row = row
                    best_col = col
                    best_value = value_knight

    if best_value > 0:
        matrix[best_row][best_col] = 0
        removed_knight += 1
    else:
        print(removed_knight)
        break











