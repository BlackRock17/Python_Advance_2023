from itertools import permutations


def possible_permutations(info: list):
    for el in permutations(info):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]