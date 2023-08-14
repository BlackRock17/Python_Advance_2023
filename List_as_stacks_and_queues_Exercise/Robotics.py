from collections import deque
from datetime import timedelta, datetime

robots = input().split(";")
time = datetime.strptime(input(), "%H:%M:%S")

robots_info = []
products = deque()

for r in robots:
    robot = {}
    info = r.split("-")
    robot["name"] = info[0]
    robot["processing_time"] = int(info[1])
    robot["available_time"] = time
    robots_info.append(robot)

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    time += timedelta(seconds=1)

    for rob in robots_info:
        if rob["available_time"] <= time:
            rob["available_time"] = time + timedelta(seconds=rob["processing_time"])
            print(f"{rob['name']} - {products.popleft()} [{datetime.strftime(time, '%H:%M:%S')}]")
            break
    else:
        products.rotate(-1)
