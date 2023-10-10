from collections import deque

caffeine = deque(list(map(int, input().split(", "))))
energy = deque(list(map(int, input().split(", "))))
stamat = 0

while caffeine and energy:
    caf = caffeine.pop()
    drink = energy.popleft()
    total = caf * drink

    if total + stamat <= 300:
        stamat += total

    else:
        energy.append(drink)
        stamat -= 30
        if stamat < 0:
            stamat = 0

if energy:
    print(f"Drinks left: {', '.join(list(map(str, energy)))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat} mg caffeine.")

