from collections import deque

numbers = deque(input().split())

mid_line = deque()

operators = "*+-/"

while numbers:
    if numbers[0] not in operators:
        mid_line.append(numbers.popleft())

    elif numbers[0] in operators:
        if numbers[0] == "*":
            while len(mid_line) > 1:
                first = int(mid_line.popleft())
                second = int(mid_line.popleft())
                mid_line.appendleft(first * second)
        elif numbers[0] == "+":
            while len(mid_line) > 1:
                first = int(mid_line.popleft())
                second = int(mid_line.popleft())
                mid_line.appendleft(first + second)
        elif numbers[0] == "-":
            while len(mid_line) > 1:
                first = int(mid_line.popleft())
                second = int(mid_line.popleft())
                mid_line.appendleft(first - second)
        elif numbers[0] == "/":
            while len(mid_line) > 1:
                first = int(mid_line.popleft())
                second = int(mid_line.popleft())
                mid_line.appendleft(int(first / second))
        numbers.popleft()

print(*mid_line)
