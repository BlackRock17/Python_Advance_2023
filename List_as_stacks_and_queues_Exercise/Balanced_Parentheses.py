text = input()

balanced = True
parenthes = []

open_paranthes = "{[("
for el in text:
    if el in open_paranthes:
        parenthes.append(el)

    else:
        if not parenthes:
            balanced = False
            break
        elif el == ")" and parenthes[-1] == "(":
            parenthes.pop()
        elif el == "]" and parenthes[-1] == "[":
            parenthes.pop()
        elif el == "}" and parenthes[-1] == "{":
            parenthes.pop()
        else:
            balanced = False
            break

if balanced:
    print("YES")
else:
    print("NO")




