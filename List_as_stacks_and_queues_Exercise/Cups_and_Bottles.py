from collections import deque

cups = deque(int(x) for x in input().split())
bottels = deque(int(x) for x in input().split())
wasted_litters = 0

while cups and bottels:
    bottel = bottels.pop()

    if bottel >= cups[0]:
        wasted_litters += bottel - cups[0]
        cups.popleft()
    else:
        cups[0] -= bottel

if bottels:
    bottels = [str(x) for x in bottels]
    print(f"Bottles: {' '.join(reversed(bottels))}")
elif cups:
    cups = [str(x) for x in cups]
    print(f"Cups: {' '.join(cups)}")

print(f"Wasted litters of water: {wasted_litters}")
