rows, cols = [int(x) for x in input().split(', ')]
matrix = []
my_row = 0
my_col = 0
decorations = 0
gifts = 0
cookies = 0
av_decorations = 0
av_gifts = 0
av_cookies = 0
all_found = False
for row in range(rows):
    data = input().split()
    matrix.append(data)
    for col in range(cols):
        element = data[col]
        if element == 'Y':
            my_row = row
            my_col = col
        if element == "D":
            av_decorations += 1
        if element == "C":
            av_cookies += 1
        if element == "G":
            av_gifts += 1

current_row = 0
current_col = 0
command = input()
while not command == "End":
    data = command.split('-')
    direction = data[0]
    steps = int(data[1])
    matrix[my_row][my_col] = 'x'
    if direction == "left":
        for i in range(steps):
            current_col = my_col - 1
            current_row = my_row
            if current_col < 0:
                current_col = cols - 1
            if matrix[current_row][current_col] == "D":
                decorations += 1
            if matrix[current_row][current_col] == "C":
                cookies += 1
            if matrix[current_row][current_col] == "G":
                gifts += 1
            matrix[current_row][current_col] = 'x'
            my_row = current_row
            my_col = current_col
            if cookies == av_cookies and decorations == av_decorations and gifts == av_gifts:
                all_found = True
                break
        matrix[my_row][my_col] = 'Y'

    elif direction == "up":
        for i in range(steps):
            current_col = my_col
            current_row = my_row - 1
            if current_row < 0:
                current_row = rows - 1
            if matrix[current_row][current_col] == "D":
                decorations += 1
            if matrix[current_row][current_col] == "C":
                cookies += 1
            if matrix[current_row][current_col] == "G":
                gifts += 1
            matrix[current_row][current_col] = 'x'
            my_row = current_row
            my_col = current_col
            if cookies == av_cookies and decorations == av_decorations and gifts == av_gifts:
                all_found = True
                break
        matrix[my_row][my_col] = 'Y'
    elif direction == "down":
        for i in range(steps):
            current_col = my_col
            current_row = my_row + 1
            if current_row == rows:
                current_row = 0
            if matrix[current_row][current_col] == "D":
                decorations += 1
            if matrix[current_row][current_col] == "C":
                cookies += 1
            if matrix[current_row][current_col] == "G":
                gifts += 1
            matrix[current_row][current_col] = 'x'
            my_row = current_row
            my_col = current_col
            if cookies == av_cookies and decorations == av_decorations and gifts == av_gifts:
                all_found = True
                break
        matrix[my_row][my_col] = 'Y'
    elif direction == "right":
        for i in range(steps):
            current_col = my_col + 1
            current_row = my_row
            if current_col == cols:
                current_col = 0
            if matrix[current_row][current_col] == "D":
                decorations += 1
            if matrix[current_row][current_col] == "C":
                cookies += 1
            if matrix[current_row][current_col] == "G":
                gifts += 1
            matrix[current_row][current_col] = 'x'
            my_row = current_row
            my_col = current_col
            if cookies == av_cookies and decorations == av_decorations and gifts == av_gifts:
                all_found = True
                break
        matrix[my_row][my_col] = 'Y'

    if all_found:
        break
    command = input()


if all_found:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
for row in matrix:
    print(*row)
