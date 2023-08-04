from collections import deque

dispenser = int(input())

person = deque()

while True:
    name = input()
    if name == "Start":
        break
    person.append(name)

while True:
    command = input()

    if command == "End":
        print(f"{dispenser} liters left")
        break

    command = command.split()

    if "refill" in command:
        dispenser += int(command[1])
    else:
        liters = int(command[0])
        if liters <= dispenser:
            dispenser -= liters
            print(f"{person.popleft()} got water")
        else:
            print(f"{person.popleft()} must wait")


