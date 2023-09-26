from collections import deque

chocolate = deque(map(int, input().split(", ")))
milk_cups = deque(map(int, input().split(", ")))

milkshakes = 0

while chocolate and milk_cups and milkshakes < 5:
    choc = chocolate[-1]
    milk = milk_cups[0]

    if choc <= 0 or milk <= 0:
        if choc <= 0:
            chocolate.pop()
        if milk <= 0:
            milk_cups.popleft()
        continue

    if choc == milk:
        chocolate.pop()
        milk_cups.popleft()
        milkshakes += 1

    else:
        milk_cups.append(milk_cups.popleft())
        chocolate[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print("Chocolate: ", end="")
    print(*chocolate, sep=", ")
else:
    print("Chocolate: empty")

if milk_cups:
    print("Milk: ", end="")
    print(*milk_cups, sep=", ")
else:
    print("Milk: empty")

### SECOND SOLUTION

from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups = deque(int(x) for x in input().split(", "))
milkshakes = 0

while milkshakes != 5 and len(chocolates) > 0 and len(cups) > 0:
    if chocolates[-1] < 1 or cups[0] < 1:
        if chocolates[-1] < 1:
            chocolates.pop()

        if cups[0] < 1:
            cups.popleft()
        continue

    chocolate = chocolates.pop()
    cup = cups.popleft()

    if chocolate == cup:
        milkshakes += 1
        continue

    else:
        cups.append(cup)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    chocolates = [str(x) for x in chocolates]
    print(f"Chocolate: {', '.join(chocolates)}")
else:
    print("Chocolate: empty")

if cups:
    cups = [str(x) for x in cups]
    print(f"Milk: {', '.join(cups)}")
else:
    print("Milk: empty")
