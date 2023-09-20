def func_executor(*args):
    result = ""
    for el in args:
        result += f"{el[0].__name__} - {el[0](*el[1])}" + "\n"

    return result
