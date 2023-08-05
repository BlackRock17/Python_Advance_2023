N = int(input())

parking = set()

for i in range(N):
    direction, car_num = tuple(input().split(", "))

    if direction == "IN":
        parking.add(car_num)

    elif direction == "OUT":
        parking.remove(car_num)

if parking:
    for car in parking:
        print(car)
else:
    print("Parking Lot is Empty")