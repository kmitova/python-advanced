strings = input().split()
main = ['red', 'yellow', 'blue']
secondary = {'orange': ('red', 'yellow'),
             'purple': ('blue', 'red'),
             'green': ('yellow', 'blue')}

made_colors = []

while strings:
    first_el = strings.pop(0)
    second_el = ''
    if strings:
        second_el = strings.pop()

    first_combination = first_el + second_el
    second_combination = second_el + first_el

    if first_combination in main or first_combination in secondary:
        made_colors.append(first_combination)
    elif second_combination in main or second_combination in secondary:
        made_colors.append(second_combination)
    else:
        if len(first_el) > 1:
            strings.insert(len(strings)//2, first_el[:-1])
        if len(second_el) > 1:
            strings.insert(len(strings)//2, second_el[:-1])

for i in range(len(made_colors)-1, -1, -1):
    current = made_colors[i]
    if current in secondary and any(x not in made_colors for x in secondary[current]):
        del made_colors[i]

print(made_colors)
