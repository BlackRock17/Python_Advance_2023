text = input()

stack_index = []

for index in range(len(text)):
    if text[index] == "(":
        stack_index.append(index)

    elif text[index] == ")":
        start_index = stack_index.pop()
        print(text[start_index:index + 1])


