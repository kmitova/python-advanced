rows = int(input())
matrix = []

for i in range(rows):
    nums = [int(x) for x in input().split(', ')]
    matrix.append(nums)

primary = []
secondary = []

for ind in range(rows):
    primary.append(matrix[ind][ind])
    secondary.append(matrix[ind][rows - 1 - ind])

print(f"Primary diagonal: {', '.join(str(el) for el in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(el) for el in secondary)}. Sum: {sum(secondary)}")
