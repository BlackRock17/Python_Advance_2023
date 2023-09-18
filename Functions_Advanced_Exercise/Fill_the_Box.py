def fill_the_box(height: int, length: int, width: int, *args):
    size = height * length * width
    cubes = 0

    for el in args:
        if el == "Finish":
            break
        cubes += int(el)

    if size > cubes:
        return f"There is free space in the box. You could put {size - cubes} more cubes."
    else:
        return f"No more free space! You have {cubes - size} more cubes."


