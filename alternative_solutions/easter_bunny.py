size = int(input())

bunny_row = 0
bunny_col = 0
max_eggs = float('-inf')
path = []
matrix = []
for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        element = data[col]
        if element == "B":
            bunny_row = row
            bunny_col = col

# for row in matrix:
#     print(*row)
# right
right_eggs = None
right_path = []
trap = False
for row in range(size):
    for col in range(size):
        if matrix[row][col] == matrix[bunny_row][bunny_col]:
            for i in range(col+1, size):
                if matrix[row][i] == 'X':
                    trap = True
                    break
                else:
                    if right_eggs == None:
                        right_eggs = 0
                    right_eggs += int(matrix[row][i])
                    right_path.append([row, i])
        if trap:
            break
    if trap:
        break

trap = False
left_eggs = None
left_path = []
for row in range(size):
    for col in range(size):
        if matrix[row][col] == matrix[bunny_row][bunny_col]:
            for i in range(col-1, -1, -1):
                if matrix[row][i] == 'X':
                    trap = True
                    break
                else:
                    if left_eggs == None:
                        up_eggs = 0
                    left_eggs += int(matrix[row][i])
                    left_path.append([row, i])
        if trap:
            break
    if trap:
        break

trap = False
up_eggs = None
up_path = []
for row in range(size):
    for col in range(size):
        if matrix[row][col] == matrix[bunny_row][bunny_col]:
            for i in range(row-1, -1, -1):
                if matrix[i][col] == 'X':
                    trap = True
                    break
                else:
                    if up_eggs == None:
                        up_eggs = 0
                    up_eggs += int(matrix[i][col])
                    up_path.append([i, col])
        if trap:
            break
    if trap:
        break

trap = False
down_eggs = None
down_path = []
for row in range(size):
    for col in range(size):
        if matrix[row][col] == matrix[bunny_row][bunny_col]:
            for i in range(row+1, size):
                if matrix[i][col] == 'X':
                    trap = True
                    break
                else:
                    if down_eggs == None:
                        down_eggs = 0
                    down_eggs += int(matrix[i][col])
                    down_path.append([i, col])
        if trap:
            break
    if trap:
        break

# if right_eggs >= 1:
if right_path and right_eggs:
    if left_eggs and right_eggs > left_eggs:
        if up_eggs and right_eggs > up_eggs:
            if down_eggs and right_eggs > down_eggs:

                max_eggs = right_eggs
                path = right_path
                print('right')

# if left_eggs >= 1:
if left_path and left_eggs:
    if right_eggs and left_eggs > right_eggs:
         if down_eggs and left_eggs > down_eggs:
             if up_eggs and left_eggs > up_eggs:

                max_eggs = left_eggs
                path = left_path
                print('left')
# if down_eggs >= 1:
if down_path and left_eggs:
    if right_eggs and down_eggs > right_eggs:
        if left_eggs and down_eggs > left_eggs:
            if up_eggs and down_eggs > up_eggs:

                path = down_path
                max_eggs = down_eggs
                print('down')
# if up_eggs >= 1:
if up_path and up_eggs:
    if down_eggs and up_eggs > down_eggs:
        if left_eggs and up_eggs > left_eggs:
            if right_eggs and up_eggs > right_eggs:

                path = up_path
                max_eggs = up_eggs
                print('up')
print(right_path)
print(right_eggs)
if len(path) > 0:
    for step in path:
        print(step)
# print(*path, sep='\n')
if max_eggs == float('-inf'):

    print(0)

else:
    print(max_eggs)

"""
5
B -1 -2 -3 -20
X 5 4 X 63
7 3 21 95 1
3 1 73 4 9
9 2 33 2 0

"""