from collections import deque

prc_bullet = int(input())
size_barrel = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
intelligence = int(input())

barrel = size_barrel
while bullets and locks:
    bullet = bullets.pop()
    intelligence -= prc_bullet
    barrel -= 1

    if bullet <= locks[0]:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    if barrel == 0 and len(bullets) > 0:
        barrel = size_barrel
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence}")