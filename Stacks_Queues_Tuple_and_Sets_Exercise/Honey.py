from collections import deque

bees = deque(int(x) for x in input().split())
nectars = deque(int(x) for x in input().split())
symbols = deque(input().split())

total_honey = 0

while bees and nectars:
    bee = bees[0]
    nectar = nectars.pop()

    if bee == 0 and nectar == 0:
        bees.popleft()
        symbols.popleft()
        continue

    if nectar == 0:
        continue

    if bee <= nectar:
        symbol = symbols.popleft()
        if symbol == "+":
            total_honey += abs(bee + nectar)
        elif symbol == "-":
            total_honey += abs(bee - nectar)
        elif symbol == "*":
            total_honey += abs(bee * nectar)
        else:
            total_honey += abs(bee / nectar)
        bees.popleft()

print(f"Total honey made: {total_honey}")
if bees:
    print("Bees left: ", end="")
    print(*bees, sep=", ")
if nectars:
    print("Nectar left: ", end="")
    print(*nectars, sep=", ")


