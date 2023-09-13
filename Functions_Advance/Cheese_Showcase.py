def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""

    for key, value in sorted_cheeses:
        sorted_value = sorted(value, reverse=True)
        result += key + "\n"
        result += "\n".join([str(el) for el in sorted_value]) + "\n"
    return result




