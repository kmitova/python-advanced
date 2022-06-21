rows, cols = [int(x) for x in input().split(',')]
matrix = []
player_row = 0
player_col = 0
decorations = 0
gifts = 0
cookies = 0
all_decorations = 0
all_gifts = 0
all_cookies = 0
items_collected = False

for row in range(rows):
    data = input().split()
    matrix.append(data)
    for col in range(cols):
        element = data[col]
        if element == "Y":
            player_row = row
            player_col = col
        if element == 'D':
            all_decorations += 1
        if element == 'C':
            all_cookies += 1
        if element == 'G':
            all_gifts += 1

command = input()
while not command == "End":
    matrix[player_row][player_col] = 'x'
    info = command.split('-')
    direction = info[0]
    steps = int(info[1])
    if direction == 'right':
        for i in range(steps):
            player_col += 1
            if player_col >= cols:
                player_col = 0
            if matrix[player_row][player_col] == 'C':
                cookies += 1
            if matrix[player_row][player_col] == 'D':
                decorations += 1
            if matrix[player_row][player_col] == 'G':
                gifts += 1
            matrix[player_row][player_col] = 'x'
            if cookies == all_cookies and gifts == all_gifts and decorations == all_decorations:
                items_collected = True
                break
        matrix[player_row][player_col] = 'Y'

    if direction == 'left':
        for i in range(steps):
            player_col -= 1
            if player_col < 0:
                player_col = cols-1
            if matrix[player_row][player_col] == 'C':
                cookies += 1
            if matrix[player_row][player_col] == 'D':
                decorations += 1
            if matrix[player_row][player_col] == 'G':
                gifts += 1
            matrix[player_row][player_col] = 'x'
            if cookies == all_cookies and gifts == all_gifts and decorations == all_decorations:
                items_collected = True
                break
        matrix[player_row][player_col] = 'Y'
    if direction == 'down':
        for i in range(steps):
            player_row += 1
            if player_row >= rows:
                player_row = 0
            if matrix[player_row][player_col] == 'C':
                cookies += 1
            if matrix[player_row][player_col] == 'D':
                decorations += 1
            if matrix[player_row][player_col] == 'G':
                gifts += 1
            matrix[player_row][player_col] = 'x'
            if cookies == all_cookies and gifts == all_gifts and decorations == all_decorations:
                items_collected = True
                break
        matrix[player_row][player_col] = 'Y'
    if direction == 'up':
        for i in range(steps):
            player_row -= 1
            if player_row < 0:
                player_row = rows-1
            if matrix[player_row][player_col] == 'C':
                cookies += 1
            if matrix[player_row][player_col] == 'D':
                decorations += 1
            if matrix[player_row][player_col] == 'G':
                gifts += 1
            matrix[player_row][player_col] = 'x'
            if cookies == all_cookies and gifts == all_gifts and decorations == all_decorations:
                items_collected = True
                break
        matrix[player_row][player_col] = 'Y'
    if items_collected:
        break
    command = input()

if items_collected:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
for row in matrix:
    print(*row)
