# 87/100

size = int(input())
matrix = []
bunny_row = 0
bunny_col = 0
max_value = 0
values = []
up_field = []
up_value = 0
down_field = []
down_value = 0
left_field = []
left_value = 0
right_field = []
right_value = 0
info = {}
for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        element = data[col]
        if element.isdigit():
            pass
        elif element == "B":
            bunny_row = row
            bunny_col = col

for row in range(size):
    for col in range(size):
        if row == bunny_row and col == bunny_col:
            # right
            right_value = 0
            right_field = []
            while 0 <= col+1 < size:
                # print(matrix[row][col+1])
                if matrix[row][col+1] == 'X':
                    break

                else:
                    right_value += int(matrix[row][col+1])
                    right_field.append([row, col+1])
                col += 1
            # print(right_value)
            values.append(right_value)
            if right_value > 0:
                info["right"] = [right_value, right_field]

for row in range(size):
    for col in range(size):
        if row == bunny_row and col == bunny_col:

            # left
            left_value = 0
            left_field = []
            while 0 <= col - 1 < size:
                # print(matrix[row][col - 1])
                if matrix[row][col - 1] == 'X':
                    break

                else:
                    left_value += int(matrix[row][col - 1])
                    left_field.append([row, col - 1])
                col -= 1
            # print(left_value)
            values.append(left_value)
            if left_value > 0:
                info["left"] = [left_value, left_field]

for row in range(size):
    for col in range(size):
        if row == bunny_row and col == bunny_col:

            # down
            down_value = 0
            down_field = []
            while 0 <= row + 1 < size:
                # print(matrix[row+1][col])
                if matrix[row+1][col] == 'X':
                    break

                else:
                    down_value += int(matrix[row+1][col])
                    down_field.append([row+1, col])
                row += 1
            # print(down_value)
            values.append(down_value)
            if down_value > 0:
                info["down"] = [down_value, down_field]

for row in range(size):
    for col in range(size):
        if row == bunny_row and col == bunny_col:

            # up
            up_value = 0
            up_field = []
            while 0 <= row -1 < size:
                # print(matrix[row-1][col])
                if matrix[row-1][col] == 'X':
                    break

                else:
                    up_value += int(matrix[row-1][col])
                    up_field.append([row-1, col])
                row -= 1
            # print(up_value)
            values.append(up_value)
            if up_value > 0:
                info["up"] = [up_value, up_field]

max_value = 0
max_direction = ''
max_field = []
for direction, value in info.items():
    if value[0] > max_value:
        max_value = value[0]
        max_direction = direction
        max_field = value[1]

print(max_direction)
if max_field:
    for row in max_field:
        print(row)
if max_value > 0:
    print(max_value)



