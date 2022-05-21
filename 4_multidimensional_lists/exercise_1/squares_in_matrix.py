rows, cols = [int(el) for el in input().split()]

matrix = []
squares = 0
for i in range(rows):
    data = input().split()
    matrix.append(data)

for row_index in range(rows-1):
    for col_index in range(cols-1):
        submatrix = [matrix[row_index][col_index], matrix[row_index][col_index+1],
                     matrix[row_index+1][col_index], matrix[row_index+1][col_index+1]]

        if matrix[row_index][col_index] == matrix[row_index][col_index+1]\
                == matrix[row_index+1][col_index] == matrix[row_index+1][col_index+1]:
            squares += 1

print(squares)
