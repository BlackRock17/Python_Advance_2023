N = int(input())

result = set()

for i in range(N):
    text = set(input().split())
    result = result.union(text)

for el in result:
    print(el)
    