string = input()
size = int(input())
player_row = 0
player_col = 0
matrix = []

for row in range(size):
    data = list(input())
    matrix.append(data)
    for col in range(size):
        element = data[col]
        if element == "P":
            player_row = row
            player_col = col


n = int(input())

for i in range(n):
    direction = input()
    matrix[player_row][player_col] = '-'
    if direction == 'right':
        if player_col + 1 < size:
            player_col = player_col + 1
            if matrix[player_row][player_col] != '-':
                string += matrix[player_row][player_col]
        else:
            if string:
                string = string[:-1]
    elif direction == 'left':
        if player_col - 1 >= 0:
            player_col = player_col - 1
            if matrix[player_row][player_col] != '-':
                string += matrix[player_row][player_col]
        else:
            if string:
                string = string[:-1]
    elif direction == 'down':
        if player_row + 1 < size:
            player_row = player_row + 1
            if matrix[player_row][player_col] != '-':
                string += matrix[player_row][player_col]
        else:
            if string:
                string = string[:-1]
    elif direction == 'up':
        if player_row - 1 >= 0:
            player_row = player_row - 1
            if matrix[player_row][player_col] != '-':
                string += matrix[player_row][player_col]
        else:
            if string:
                string = string[:-1]

matrix[player_row][player_col] = 'P'
print(string)
for row in matrix:
    print(*row, sep='')
    