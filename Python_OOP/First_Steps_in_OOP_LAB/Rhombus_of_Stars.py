def print_rhombus(n, row):
    for _ in range(n - row):
        print(" ", end="")
    print(f"* " * row)


n = int(input())

for row in range(1, n + 1):
    print_rhombus(n, row)

for row in range(n - 1, -1, -1):
    print_rhombus(n, row)


