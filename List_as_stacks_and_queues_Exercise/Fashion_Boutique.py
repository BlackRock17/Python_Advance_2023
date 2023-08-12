clothes = list(map(int, input().split()))
rack_cap = int(input())

total_rack = 0

while clothes:
    current_cap = rack_cap

    while True:
        if clothes[-1] <= current_cap:
            current_cap -= clothes.pop()

        if not clothes:
            break

        if clothes[-1] > current_cap:
            break

    total_rack += 1

print(total_rack)