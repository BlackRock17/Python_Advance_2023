def reverse_text(string):
    text = list(string)

    while text:
        yield text.pop()

for char in reverse_text("step"):
    print(char, end='')
