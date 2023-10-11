def forecast(*args):
    result = {"Sunny": [], "Cloudy": [], "Rainy": []}
    for el in args:
        result[el[1]].append(el[0])

    for key, value in result.items():
        result[key] = sorted(value)

    output = ""

    for weather, towns in result.items():
        for town in towns:
            output += f"{town} - {weather}" + "\n"

    return output

