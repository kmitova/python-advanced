def math_operations(*args, **kwargs):
    result = ''
    counter = 1
    for num in args:
        if counter == 1:
            kwargs['a'] += num
            counter += 1
        elif counter == 2:
            kwargs['s'] -= num
            counter += 1
        elif counter == 3:
            if num != 0:
                kwargs['d'] /= num
            counter += 1
        elif counter == 4:
            kwargs['m'] *= num
            counter = 1

    sorted_values = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    for key, value in sorted_values:
        result += f"{key}: {value:.1f}\n"
    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
