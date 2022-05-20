rows, cols = [int(el) for el in input().split(', ')]
matrix = []

for i in range(rows):
    data = [int(x) for x in input().split(', ')]
    matrix.append(data)

max_sum = 0
max_matrix = []
for row_index in range(rows-1):
    for col_index in range(cols-1):
        submatrix = [matrix[row_index][col_index], matrix[row_index][col_index+1],
                     matrix[row_index+1][col_index], matrix[row_index+1][col_index+1]]
        current_sum = sum(submatrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = submatrix

print(*max_matrix[:2])
print(*max_matrix[2:])
print(max_sum)



