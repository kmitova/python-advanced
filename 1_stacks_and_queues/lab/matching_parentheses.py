expression = input()

parentheses_stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        parentheses_stack.append(index)
    elif expression[index] == ")":
        start_index = parentheses_stack.pop()
        print(expression[start_index: index+1])
