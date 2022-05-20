n = int(input())

rows = n
cols = n

diagonal_sum = 0
matrix = []
for i in range(n):
    data = [int(x) for x in input().split()]
    matrix.append(data)

# print(matrix)
ind = 0

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        if col_index == ind:
            diagonal_sum += matrix[row_index][col_index]
    ind += 1

print(diagonal_sum)

