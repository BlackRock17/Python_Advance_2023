rows, cols = map(int, input().split())
text = input()
counter = 0

for row in range(rows):
    result = ""
    for col in range(cols):
        result += text[counter % len(text)]
        counter += 1
    if row % 2 == 0:
        print(result)
    else:
        print(result[::-1])
