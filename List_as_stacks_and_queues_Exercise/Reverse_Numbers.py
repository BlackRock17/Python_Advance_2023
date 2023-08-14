numbers = list(map(int, input().split()))

reverse_num = []

for i in range(len(numbers)):
    reverse_num.append(numbers.pop())

print(*reverse_num, sep=" ")