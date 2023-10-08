def add_songs(*args):
    result = {}

    for el in args:
        title = el[0]
        lyrics = el[1]

        if title not in result.keys():
            result[title] = lyrics
        else:
            result[title].extend(lyrics)

    output = ""

    for key, value in result.items():
        output += f"- {key}" + "\n"

        if value:
            for row in value:
                output += f"{row}" + "\n"

    return output


