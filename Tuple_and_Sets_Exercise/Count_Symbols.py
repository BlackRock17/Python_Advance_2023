text = input()

result = {}

for el in text:
    if el not in result:
        result[el] = 0
    result[el] += 1

for key, value in sorted(result.items()):
    print(f"{key}: {value} time/s")
