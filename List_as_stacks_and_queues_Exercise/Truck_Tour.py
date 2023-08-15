from collections import deque

pumps = int(input())

info = deque()

for el in range(pumps):
    info.append(tuple(map(int, input().split())))

complete = False
tank = 0
index = 0

while True:

    for pet_dis in info:
        petrol = pet_dis[0]
        distance = pet_dis[1]

        tank += petrol

        if tank < distance:
            index += 1
            break
        else:
            tank -= distance
    else:
        complete = True

    if complete:
        break
    else:
        tank = 0
        info.rotate(-1)

print(index)