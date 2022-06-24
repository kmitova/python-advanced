size = int(input())
bombs = int(input())
matrix = []
row_length = []

for i in range(size):
    row_length.append(0)
for row in range(size):
    data = list('0' * size)
    matrix.append([int(x) for x in data])

for i in range(bombs):
    coords = input()
    coords = coords.replace('(', '')
    coords = coords.replace(')', '')
    info = coords.split(', ')
    row = int(info[0])
    col = int(info[1])
    matrix[row][col] = '*'

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == '*':
            #right
            if col + 1 < size:
                if matrix[row][col+1] != '*':
                    matrix[row][col+1] = int(matrix[row][col+1])
                    matrix[row][col+1] += 1
            #left
            if col - 1 >= 0:
                if matrix[row][col-1] != '*':
                    matrix[row][col-1] = int(matrix[row][col-1])
                    matrix[row][col-1] += 1
            #down
            if row + 1 < size:
                if matrix[row+1][col] != '*':
                    matrix[row+1][col] = int(matrix[row+1][col])
                    matrix[row+1][col] += 1
            #up
            if row - 1 >= 0:
                if matrix[row-1][col] != '*':
                    matrix[row-1][col] = int(matrix[row-1][col])
                    matrix[row-1][col] += 1
            #down right
            if row + 1 < size and col + 1 < size:
                if matrix[row+1][col+1] != '*':
                    matrix[row+1][col+1] = int(matrix[row+1][col+1])
                    matrix[row+1][col+1] += 1
            #down left
            if row + 1 < size and col - 1 >= 0:
                if matrix[row+1][col-1] != '*':
                    matrix[row+1][col-1] = int(matrix[row+1][col-1])
                    matrix[row+1][col-1] += 1
            # up left
            if row - 1 >= 0 and col - 1 >= 0:
                if matrix[row-1][col-1] != '*':
                    matrix[row-1][col-1] = int(matrix[row-1][col-1])
                    matrix[row-1][col-1] += 1
            #up right
            if row - 1 >= 0 and col + 1 < size:
                if matrix[row - 1][col + 1] != '*':
                    matrix[row - 1][col + 1] = int(matrix[row - 1][col + 1])
                    matrix[row - 1][col + 1] += 1
for row in matrix:
    print(*row)
