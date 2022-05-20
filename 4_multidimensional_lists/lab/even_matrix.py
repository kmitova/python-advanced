# matrix = []
rows = int(input())

# for i in range(rows):
#
#     nums = [int(el) for el in input().split(', ') if int(el) % 2 == 0]
#     matrix.append(nums)

# with comprehension
matrix = [[int(el) for el in input().split(', ') if int(el) % 2 == 0] for i in range(rows)]

print(matrix)
