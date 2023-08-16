N = int(input())

odd = set()
even = set()

for i in range(1, N + 1):
    name = input()
    total_sum = 0

    for char in name:
        total_sum += ord(char)

    total_sum = int(total_sum / i)

    if total_sum % 2 == 0:
        even.add(total_sum)
    else:
        odd.add(total_sum)

if sum(odd) == sum(even):
    total = list(even.union(odd))

elif sum(odd) > sum(even):
    total = list(odd.difference(even))
else:
    total = list(even.symmetric_difference(odd))

print(*total, sep=", ")

