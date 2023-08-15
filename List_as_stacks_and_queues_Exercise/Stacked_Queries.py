N = int(input())

stack = []

for i in range(N):
    command = input().split()
    number = command[0]

    if number == "1":
        stack.append(int(command[1]))

    elif number == "2":
        if stack:
            stack.pop()

    elif number == "3":
        if stack:
            print(max(stack))

    elif number == "4":
        if stack:
            print(min(stack))

stack = reversed(stack)
if stack:
    print(*stack, sep=", ")
