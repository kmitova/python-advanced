matrix = []
size = int(input())

for row in range(size):
    data = [int(x) for x in input().split()]
    matrix.append(data)

coordinates = input().split()

for el in coordinates:
    info = [int(x) for x in el.split(',')]
    row = info[0]
    col = info[1]
    if matrix[row][col] and matrix[row][col] > 0:
        value = matrix[row][col]
        matrix[row][col] = 0
#         right
        if col + 1 < size and matrix[row][col+1] > 0:
            matrix[row][col + 1] -= value
        # left
        if col - 1 >= 0 and matrix[row][col-1] > 0:
            matrix[row][col - 1] -= value
        # down
        if row + 1 < size and matrix[row+1][col] > 0:
            matrix[row+1][col] -= value
        # up
        if row - 1 >= 0 and matrix[row-1][col] > 0:
            matrix[row-1][col] -= value
        # up right
        if row - 1 >= 0 and col+1 < size and matrix[row-1][col+1] > 0:
            matrix[row-1][col+1] -= value
        # up left
        if row - 1 >= 0 and col -1 >= 0 and matrix[row-1][col-1] > 0:
            matrix[row-1][col-1] -= value
        #  down right
        if row + 1 < size and col+1 < size and matrix[row+1][col+1] > 0:
            matrix[row+1][col+1] -= value
        # down left
        if row+1 < size and col-1 >= 0 and matrix[row+1][col-1] > 0:
            matrix[row+1][col-1] -= value


alive = 0
alive_sum = 0

for row in matrix:
    for el in row:
        if el > 0:
            alive += 1
            alive_sum += el

print(f"Alive cells: {alive}")
print(f"Sum: {alive_sum}")
for row in matrix:
    print(*row)
