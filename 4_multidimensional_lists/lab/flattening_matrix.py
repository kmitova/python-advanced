rows = int(input())
matrix = []
for i in range(rows):
    nums = [int(x) for x in input().split(', ')]
    matrix.extend(nums)

print(matrix)

