from collections import deque

def math_operations(*args, **kwargs):
    numbers = deque(args)
    result = ""

    while numbers:
        for key, value in kwargs.items():
            if len(numbers) == 0:
                break
            if key == "a":
                kwargs[key] += numbers.popleft()
            elif key == "s":
                kwargs[key] -= numbers.popleft()
            elif key == "d":
                num = numbers.popleft()
                if num == 0:
                    continue
                else:
                    kwargs[key] /= num
            elif key == "m":
                kwargs[key] *= numbers.popleft()
    kwargs = dict(sorted(kwargs.items(), key=lambda x: (-x[1], x[0])))
    for k, w in kwargs.items():
        result += f"{k}: {w:.1f}" + "\n"

    return result

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))