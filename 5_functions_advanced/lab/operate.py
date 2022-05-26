def operate(op, *args):
    if op == '+' or op == '-' or op == '/':
        result = 0
    else:
        result = 1

    if op == '+':
        for el in args:
            result += el
    elif op == '-':
        result = args[0]
        for el in args[1:]:
            result -= el
    elif op == "*":
        for el in args:
            result *= el
    elif op == "/":
        result = args[0]
        for el in args[1:]:
            result /= el

    return result


print(operate("-", 1, 4 ,5 ,6))
print(operate("*", 3, 4))
