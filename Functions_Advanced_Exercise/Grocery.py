def grocery_store(**kwargs):
    sorted_items = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = ""

    for p, q in sorted_items:
        result += f"{p}: {q}" + "\n"

    return result


