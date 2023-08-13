from collections import deque

food = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

while orders:
    if orders[0] > food:
        break

    else:
        food -= orders.popleft()

orders = list(map(str, orders))

if not orders:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(orders)}")