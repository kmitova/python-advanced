from sys import maxsize

max_sum = -maxsize
max_matrix = []
rows, cols = [int(el) for el in input().split()]

matrix = []

for i in range(rows):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)


for row_index in range(rows-2):
    for col_index in range(cols-2):
        current_sum = matrix[row_index][col_index] + matrix[row_index][col_index+1] + matrix[row_index][col_index+2] +\
            matrix[row_index+1][col_index] + matrix[row_index+1][col_index + 1] + matrix[row_index+1][col_index + 2] + \
                      matrix[row_index+2][col_index] + matrix[row_index+2][col_index + 1] + matrix[row_index+2][col_index+2]

        submatrix = [matrix[row_index][col_index], matrix[row_index][col_index+1], matrix[row_index][col_index+2],
            matrix[row_index+1][col_index], matrix[row_index+1][col_index + 1], matrix[row_index+1][col_index + 2],
                      matrix[row_index+2][col_index], matrix[row_index+2][col_index + 1], matrix[row_index+2][col_index+2]]
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = submatrix

print(f"Sum = {max_sum}")
print(' '.join(str(el) for el in max_matrix[:3]))
print(' '.join(str(el) for el in max_matrix[3:6]))
print(' '.join(str(el) for el in max_matrix[6:9]))
