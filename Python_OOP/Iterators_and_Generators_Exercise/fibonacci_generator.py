def fibonacci():
    num1, num2 = 0, 1

    while True:
        yield num1

        sum_ = num1 + num2
        num1 = num2
        num2 = sum_

generator = fibonacci()
for i in range(1):
    print(next(generator))

