from collections import deque

people = deque(input().split())
n_toss = int(input())

while len(people) > 1:
    people.rotate(-n_toss + 1)
    print(f"Removed {people.popleft()}")

print(f"Last is {people[0]}")