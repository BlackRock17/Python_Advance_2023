from collections import deque

materials = deque([int(x) for x in input().split()])
magic_values = deque([int(x) for x in input().split()])

present = {"Bicycle": 0, "Doll": 0, "Teddy bear": 0, "Wooden train": 0}

while materials and magic_values:
    material = materials.pop()
    magic = magic_values.popleft()
    multi_sum = material * magic

    if material == 0 or magic == 0:
        if material != 0:
            materials.append(material)
        if magic != 0:
            magic_values.appendleft(magic)
        continue

    if multi_sum == 150:
        present["Doll"] += 1

    elif multi_sum == 250:
        present["Wooden train"] += 1

    elif multi_sum == 300:
        present["Teddy bear"] += 1

    elif multi_sum == 400:
        present["Bicycle"] += 1

    elif multi_sum < 0:
        materials.append(material + magic)

    elif multi_sum > 0:
        materials.append(material + 15)

if (present["Doll"] and present["Wooden train"]) or (present["Teddy bear"] and present["Bicycle"]):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    materials.reverse()
    print("Materials left: ", end="")
    print(*materials, sep=", ")

if magic_values:
    print("Magic left: ", end="")
    print(*magic_values, sep=", ")

for key, value in present.items():
    if value:
        print(f"{key}: {value}")

