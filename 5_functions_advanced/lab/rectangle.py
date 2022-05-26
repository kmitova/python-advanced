def rectangle(length, width):
    def area(length, width):
        return f"Rectangle area: {length * width}"

    def perimeter(length, width):
        return f"Rectangle perimeter: {2 * length + 2 * width}"

    if isinstance(length, str) or isinstance(width, str):
        return "Enter valid values!"
    else:
        result = area(length, width) + '\n' + perimeter(length, width)
        return result


print(rectangle(2, 10))
print(rectangle('2', 10))

