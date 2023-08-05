numbers = tuple(float(num) for num in input().split())

result = {}

for num in numbers:
    if num not in result:
        result[num] = 1
    else:
        result[num] += 1

for key, value in result.items():
    print(f"{key} - {value} times")
