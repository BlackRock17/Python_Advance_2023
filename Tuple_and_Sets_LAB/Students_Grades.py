N = int(input())

result = {}
for i in range(N):
    name, grade = tuple(input().split())

    if name not in result:
        result[name] = []

    result[name].append(float(grade))

for key, value in result.items():
    print(f"{key} -> ", end="")
    for num in value:
        print(f"{num:.2f} ", end="")
    print(f"(avg: {sum(value) / len(value):.2f})")

