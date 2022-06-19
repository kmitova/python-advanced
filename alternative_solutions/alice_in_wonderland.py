size = int(input())

alice_row = 0
alice_col = 0
matrix = []
tea = 0
out_of_field = False

for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        element = data[col]
        if element == "A":
            alice_row = row
            alice_col = col

while True:
    direction = input()
    matrix[alice_row][alice_col] = '*'
    # right
    if direction == 'right':
        if alice_col + 1 < size:
            alice_col = alice_col + 1
            if matrix[alice_row][alice_col] == 'R':
                out_of_field = True
            elif matrix[alice_row][alice_col] != '.' and matrix[alice_row][alice_col] != '*':
                tea += int(matrix[alice_row][alice_col])
        else:
            out_of_field = True
    if direction == 'left':
        if alice_col - 1 >= 0:
            alice_col = alice_col - 1
            if matrix[alice_row][alice_col] == 'R':
                out_of_field = True
            elif matrix[alice_row][alice_col] != '.' and matrix[alice_row][alice_col] != '*':
                tea += int(matrix[alice_row][alice_col])
        else:
            out_of_field = True
    if direction == 'up':
        if alice_row - 1 >= 0:
            alice_row = alice_row - 1
            if matrix[alice_row][alice_col] == 'R':
                out_of_field = True
            elif matrix[alice_row][alice_col] != '.' and matrix[alice_row][alice_col] != '*':
                tea += int(matrix[alice_row][alice_col])
        else:
            out_of_field = True
    if direction == 'down':
        if alice_row + 1 < size:
            alice_row = alice_row + 1
            if matrix[alice_row][alice_col] == 'R':
                out_of_field = True
            elif matrix[alice_row][alice_col] != '.' and matrix[alice_row][alice_col] != '*':
                tea += int(matrix[alice_row][alice_col])
        else:
            out_of_field = True
    matrix[alice_row][alice_col] = '*'
    if out_of_field:
        break
    if tea >= 10:
        break

if out_of_field:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for row in matrix:
    print(*row)
