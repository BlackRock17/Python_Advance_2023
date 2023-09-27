from collections import deque

subs = deque(input().split())

result = []
colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']

while subs:
    if len(subs) == 1:
        if subs[0] in colors:
            result.append(subs[0])
        break

    first_sub = subs.popleft()
    second_sub = subs.pop()

    first_col = first_sub + second_sub
    second_col = second_sub + first_sub

    if first_col in colors:
        result.append(first_col)
        continue

    elif second_col in colors:
        result.append(second_col)
        continue

    index = len(subs) // 2

    if len(first_sub) > 1:
        subs.insert(index, first_sub[:-1])
    if len(second_sub) > 1:
        subs.insert(index, second_sub[:-1])

if 'orange' in result:
    if 'red' not in result or 'yellow' not in result:
        result.remove('orange')

if 'purple' in result:
    if 'red' not in result or 'blue' not in result:
        result.remove('purple')

if 'green' in result:
    if 'blue' not in result or 'yellow' not in result:
        result.remove('green')

print(result)








