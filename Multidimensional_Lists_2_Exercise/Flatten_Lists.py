text = input().split("|")

result = []

for _ in range(len(text) - 1, - 1, - 1):
        output = text[_].split()
        if output:
            print(*output, end=" ")

    ### second_sol

numbers = input().split("|")

result = []

for el in reversed(numbers):
    nums = el.split()
    for n in nums:
        result.append(n)

print(*result)