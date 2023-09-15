def rectangle(lenght, width):
    if not isinstance(lenght, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        return f"Rectangle area: {lenght * width}"

    def perimeter():
        return f"Rectangle perimeter: {width * 2 + lenght * 2}"

    return area() + "\n" + perimeter()
