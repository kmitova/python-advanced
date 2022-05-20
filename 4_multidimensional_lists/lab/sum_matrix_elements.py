rows, cols = [int(el) for el in input().split(', ')]
matrix = []
sum_total = 0
for i in range(rows):
    numbers = [int(el) for el in input().split(', ')]
    # sum_total += sum(numbers) another way to solve the sum
    matrix.append(numbers)

for el in matrix:
    for n in el:
        sum_total += n

print(sum_total)
print(matrix)
