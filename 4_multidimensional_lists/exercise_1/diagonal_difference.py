rows = int(input())
matrix = []

for i in range(rows):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

primary = []
secondary = []

for ind in range(rows):
    primary.append(matrix[ind][ind])
    secondary.append(matrix[ind][rows - 1 - ind])

print(abs(sum(primary) - sum(secondary)))
