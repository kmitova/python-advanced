n = int(input())
rows = n
cols = n
matrix = []
for i in range(rows):
    data = list(input())
    matrix.append(data)

symbol = input()
is_found = False

for row_index in range(len(matrix)):
    for col_index in range(len(matrix)):
        el = matrix[row_index][col_index]
        if el == symbol:
            print(f"({row_index}, {col_index})")
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print(f"{symbol} does not occur in the matrix")
