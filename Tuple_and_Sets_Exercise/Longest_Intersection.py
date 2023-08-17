N = int(input())

result = list()

for _ in range(N):
    range_one, range_two = input().split("-")
    first_start, first_end = map(int, range_one.split(','))
    second_start, second_end = map(int, range_two.split(','))

    first_range = set()
    second_range = set()

    for num in range(first_start, first_end + 1):
        first_range.add(num)

    for num_ in range(second_start, second_end + 1):
        second_range.add(num_)

    current_int = first_range.intersection(second_range)

    if len(current_int) > len(result):
        result = list(current_int)

print(f"Longest intersection is {result} with length {len(result)}")

