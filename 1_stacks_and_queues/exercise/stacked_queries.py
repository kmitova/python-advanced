stack = []

n = int(input())

for i in range(n):
    query = input().split()
    command = int(query[0])
    if command == 1:
        number = int(query[1])
        stack.append(number)
    elif command == 2 and stack:
        stack.pop()
    elif command == 3 and stack:
        print(max(stack))
    elif command == 4 and stack:
        print(min(stack))

while stack:
    element = stack.pop()
    if stack:
        print(element, end=", ")
    else:
        print(element, end="")
