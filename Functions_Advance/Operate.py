def operate(operator, *args):
    if len(args) == 0:
        return 0

    def add():
        return sum(args)

    def subtraction():
        result = args[0]
        for index in range(1, len(args)):
            result -= args[index]
        return result

    def multiplication():
        result = 1
        for el in args:
            result *= el
        return result

    def division():
        result = args[0]
        for n in range(1, len(args)):
            if args[n] == 0:
                continue
            result /= args[n]
        return result

    if operator == "+":
        return add()
    elif operator == "-":
        return subtraction()
    elif operator == "*":
        return multiplication()
    elif operator == "/":
        return division()
