def even_odd(*args):
    command = args[-1]
    result = []
    if command == 'even':
        for el in args[:-1]:
            if el % 2 == 0:
                result.append(el)
    else:
        for el in args[:-1]:
            if not el % 2 == 0:
                result.append(el)
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
