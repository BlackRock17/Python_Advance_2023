def age_assignment(*args, **kwargs):
    result = ""

    for name in sorted(args):
        for letter, age in kwargs.items():
            if name[0] == letter:
                result += f"{name} is {age} years old." + "\n"

    return result
