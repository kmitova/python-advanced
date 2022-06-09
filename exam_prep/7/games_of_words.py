string = input()
size = int(input())
matrix = []
player_row = 0
player_col = 0

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
    command = input()
    matrix[player_row][player_col] = '-'
    if command == "right":
        if player_col + 1 < size:
            player_col = player_col + 1
            if matrix[player_row][player_col] != '-':
                string += matrix[player_row][player_col]
                matrix[player_row][player_col] = '-'
        else:
            if len(string) > 0:
                string = string[:-1]
    elif command == "left":
        if player_col - 1 >= 0:
            player_col = player_col - 1
            if matrix[player_row][player_col] != '-':
                string += matrix[player_row][player_col]
                matrix[player_row][player_col] = '-'
        else:
            if len(string) > 0:
                string = string[:-1]
    elif command == "down":
        if player_row + 1 < size:
            player_row = player_row + 1
            if matrix[player_row][player_col] != '-':
                string += matrix[player_row][player_col]
                matrix[player_row][player_col] = '-'
        else:
            if len(string) > 0:
                string = string[:-1]
    elif command == "up":
        if player_row - 1 >= 0:
            player_row = player_row - 1
            if matrix[player_row][player_col] != '-':
                string += matrix[player_row][player_col]
                matrix[player_row][player_col] = '-'
        else:
            if len(string) > 0:
                string = string[:-1]

matrix[player_row][player_col] = 'P'


print(string)
for row in matrix:
    row = ''.join(row)
    for el in row:
        print(el, end='')
    print()


