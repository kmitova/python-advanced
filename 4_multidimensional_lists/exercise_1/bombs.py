def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_neighbors(row, col, matrix):
    size = len(matrix)
    neighbors = []
    # CASES
    # row -1, col
    if is_inside(row-1, col, size) and matrix[row-1][col] > 0:
        neighbors.append([row-1, col])
    # row +1, col
    if is_inside(row+1, col, size) and matrix[row+1][col] > 0:
        neighbors.append([row+1, col])
    # row, col -1
    if is_inside(row, col -1, size) and matrix[row][col -1] > 0:
        neighbors.append([row, col-1])
    # row, col +1
    if is_inside(row, col+1, size) and matrix[row][col+1] > 0:
        neighbors.append([row, col+1])
    # row -1, col -1
    if is_inside(row-1, col-1, size) and matrix[row-1][col-1] > 0:
        neighbors.append([row-1, col-1])
    # row -1, col +1
    if is_inside(row-1, col+1, size) and matrix[row-1][col+1] > 0:
        neighbors.append([row-1, col+1])
    # row +1, col -1
    if is_inside(row+1, col-1, size) and matrix[row+1][col-1] > 0:
        neighbors.append([row+1, col-1])
    # row +1, col +1
    if is_inside(row+1, col+1, size) and matrix[row+1][col+1] > 0:
        neighbors.append([row+1, col+1])
    return neighbors


n = int(input())
matrix = []
for i in range(n):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

bombs = input().split()

for bomb in bombs:
    bomb_row, bomb_col = [int(x) for x in bomb.split(',')]

    if matrix[bomb_row][bomb_col] > 0:
        bomb_power = matrix[bomb_row][bomb_col]
        neighbors = get_neighbors(bomb_row, bomb_col, matrix)
        matrix[bomb_row][bomb_col] = 0
        for row, col in neighbors:
            matrix[row][col] -= bomb_power

alive = 0
total_sum = 0
for row in matrix:
    for el in row:
        if el > 0:
            alive += 1
            total_sum += el
print(f"Alive cells: {alive}")
print(f"Sum: {total_sum}")

for row in matrix:
    print(*row, sep=' ')
