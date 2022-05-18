from collections import deque

string = deque(input().split())

main = {'red', 'yellow', 'blue'}
secondary = {'orange', 'purple', 'green'}
found = []

while string:
    first = string.popleft()
    second = string.pop() if string else ""

    result = first + second
    if result in main or result in secondary:
        found.append(result)
        continue

    result = second + first
    if result in main or result in secondary:
        found.append(result)
        continue

    first = first[:-1]
    second = second[:-1]
    if first:
        string.insert(len(string)//2, first)
    if second:
        string.insert(len(string) // 2, second)

result = []
required_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

for color in found:
    if color in main:
        result.append(color)
    else:
        is_valid = True
        for required_color in required_colors[color]:
            if required_color not in found:
                is_valid = False
                break
        if is_valid:
            result.append(color)

print(result)
