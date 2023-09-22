def even_odd_filter(**kwargs):
    dictionary = {}
    for key, value in kwargs.items():
        if key == "odd":
            dictionary[key] = [x for x in value if x % 2 == 1]
        else:
            dictionary[key] = [x for x in value if x % 2 == 0]
    return dict(sorted(dictionary.items(), key=lambda x: -len(x[1])))

