N = int(input())

matrix = []

for _ in range(N):
    matrix.append(list(input()))

symbol = input()

found = False
for row in range(len(matrix)):
    for symb in range(len(matrix[row])):
        if matrix[row][symb] == symbol:
            print(f"({row}, {symb})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{symbol} does not occur in the matrix")

