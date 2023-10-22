from collections import deque

Darth_Vader_Ducky = 0
Thor_Ducky = 0
Big_Blue_Rubber_Ducky = 0
Small_Yellow_Rubber_Ducky = 0

program_times = deque([int(x) for x in input().split()])
tasks = deque([int(x) for x in input().split()])

while tasks:
    time = program_times.popleft()
    task = tasks.pop()
    total = time * task

    if total <= 60:
        Darth_Vader_Ducky += 1
    elif total <= 120:
        Thor_Ducky += 1
    elif total <= 180:
        Big_Blue_Rubber_Ducky += 1
    elif total <= 240:
        Small_Yellow_Rubber_Ducky += 1
    else:
        program_times.append(time)
        tasks.append(task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {Darth_Vader_Ducky}")
print(f"Thor Ducky: {Thor_Ducky}")
print(f"Big Blue Rubber Ducky: {Big_Blue_Rubber_Ducky}")
print(f"Small Yellow Rubber Ducky: {Small_Yellow_Rubber_Ducky}")

