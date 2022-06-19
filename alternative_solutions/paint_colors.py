from collections import deque

main = ['red', 'yellow', 'blue']
searched_colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']
string = deque(input().split())
main_found = []
secondary_found = []
colors = []
while string:
    if len(string) == 1:
        part = string[0]
        if part in searched_colors:
            colors.append(part)
        string.pop()
    else:
        part1 = string[0]
        part2 = string[-1]
        first_combination = part1 + part2
        second_combination = part2 + part1
        if first_combination in searched_colors:
            colors.append(first_combination)
            string.pop()
            string.popleft()
        elif second_combination in searched_colors:
            string.pop()
            string.popleft()
            colors.append(second_combination)
        else:
            part1 = part1[:-1]
            part2 = part2[:-1]
            string.pop()
            string.popleft()
            if part1:
                string.insert((len(string)//2), part1)
            if part2:
                string.insert((len(string)//2), part2)

result_list = []
for color in colors:
    if color in main:
        result_list.append(color)
    if color == 'orange':
        if 'yellow' in colors and 'red' in colors:
            result_list.append(color)
    if color == 'purple':
        if 'blue' in colors and 'red' in colors:
            result_list.append(color)
    if color == 'green':
        if 'yellow' in colors and 'blue' in colors:
            result_list.append(color)

print(result_list)
