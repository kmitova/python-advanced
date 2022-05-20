rows, cols = [int(el) for el in input().split(', ')]
matrix = []

for i in range(rows):
    data = [int(x) for x in input().split()]
    matrix.append(data)

for col_index in range(cols):
    result = 0
    for row_index in range(rows):
        result += matrix[row_index][col_index]
    print(result)
