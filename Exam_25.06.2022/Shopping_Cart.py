def shopping_cart(*args):
    result = {"Pizza": [], "Soup": [], "Dessert": []}

    for el in args:
        if el == "Stop":
            break
        elif el[0] == "Pizza" and len(result[el[0]]) < 4 and el[1] not in result[el[0]]:
            result[el[0]].append(el[1])
        elif el[0] == "Soup" and len(result[el[0]]) < 3 and el[1] not in result[el[0]]:
            result[el[0]].append(el[1])
        elif el[0] == "Dessert" and len(result[el[0]]) < 2 and el[1] not in result[el[0]]:
            result[el[0]].append(el[1])

    if len(result["Pizza"]) == 0 and len(result["Soup"]) == 0 and len(result["Dessert"]) == 0:
        return "No products in the cart!"

    result = dict(sorted(result.items(), key=lambda x: (-len(x[1]), x[0])))

    output = ""

    for key, value in result.items():
        output += f"{key}:" + "\n"
        if value:
            for product in sorted(value):
                output += f" - {product}" + "\n"

    return output
