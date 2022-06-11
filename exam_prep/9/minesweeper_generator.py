size = int(input())
bombs = int(input())
matrix = []

for row in range(size):
    data = list("0" * size)
    matrix.append([int(x) for x in data])

for bomb in range(bombs):
    coords = input()
    coords = coords.replace("(", "")
    coords = coords.replace(")", "")
    row_str, col_str = coords.split(", ")
    row = int(row_str)
    col = int(col_str)
    matrix[row][col] = '*'

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "*":
            # up
            if row - 1 >= 0:
                if matrix[row-1][col] != '*':
                    matrix[row-1][col] += 1
#             down
            if row + 1 < size:
                if matrix[row+1][col] != '*':

                    matrix[row+1][col] += 1
#             right
            if col + 1 < size:
                if matrix[row][col+1] != '*':
                    matrix[row][col + 1] += 1
#             left
            if col - 1 >= 0:
                if matrix[row][col-1] != '*':
                    matrix[row][col-1] += 1
#             down right
            if row + 1 < size and col + 1 < size:
                if matrix[row+1][col+1] != '*':
                    matrix[row+1][col+1] += 1
#              down left
            if row + 1 < size and col - 1 >= 0:
                if matrix[row+1][col-1] != '*':
                    matrix[row+1][col-1] += 1
#             up left
            if row - 1 >= 0 and col - 1 >= 0:
                if matrix[row-1][col-1] != '*':
                    matrix[row-1][col-1] += 1
#             up right
            if row - 1 >= 0 and col + 1 < size:
                if matrix[row-1][col+1] != '*':
                    matrix[row-1][col+1] += 1


for row in matrix:
    print(*row)
