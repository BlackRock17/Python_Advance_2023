def read_next(*args):
    for el in args:
        for sub_el in el:
            yield sub_el


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)

