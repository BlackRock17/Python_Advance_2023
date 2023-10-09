from collections import deque

seats = input().split(", ")
first_nums = deque(map(int, input().split(", ")))
second_nums = deque(map(int, input().split(", ")))
matches = []
rotations = 0

while len(matches) < 3 and rotations < 10:
    rotations += 1
    num1 = first_nums.popleft()
    num2 = second_nums.pop()
    seat_num1 = f"{num1}{chr(num1 + num2)}"
    seat_num2 = f"{num2}{chr(num1 + num2)}"

    if seat_num1 in seats:
        matches.append(seat_num1)
        seats.remove(seat_num1)
    elif seat_num2 in seats:
        matches.append(seat_num2)
        seats.remove(seat_num2)
    else:
        first_nums.append(num1)
        second_nums.appendleft(num2)

print(f"Seat matches: {', '.join(matches)}")
print(f"Rotations count: {rotations}")
