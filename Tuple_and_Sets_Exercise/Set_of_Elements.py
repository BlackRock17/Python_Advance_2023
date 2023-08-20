N, M = input().split()

first_set = set()
second_set = set()

for i in range(int(N)):
    first_set.add(input())

for k in range(int(M)):
    second_set.add(input())

result = first_set.intersection(second_set)

for num in result:
    print(num)
