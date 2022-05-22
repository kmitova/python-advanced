size = int(input())
matrix = []
alice_row = 0
alice_col = 0
tea = 0
dies = False
wins = False

for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        element = data[col]
        if element == "A":
            alice_row = row
            alice_col = col


while True:
    command = input()
    if command == "right":
        matrix[alice_row][alice_col] = "*"
        if 0 <= alice_col+1 < size:
            if matrix[alice_row][alice_col+1] == ".":
                matrix[alice_row][alice_col + 1] = '*'

            elif matrix[alice_row][alice_col+1].isdigit():
                tea += int(matrix[alice_row][alice_col+1])
                matrix[alice_row][alice_col + 1] = '*'
            elif matrix[alice_row][alice_col+1] == "R":
                matrix[alice_row][alice_col + 1] = '*'
                dies = True
                break
            alice_row = alice_row
            alice_col = alice_col+1

        else:
            dies = True
            break
    if command == "left":
        matrix[alice_row][alice_col] = "*"

        if 0 <= alice_col-1 < size:
            if matrix[alice_row][alice_col-1] == ".":
                matrix[alice_row][alice_col - 1] = '*'
            elif matrix[alice_row][alice_col-1].isdigit():
                tea += int(matrix[alice_row][alice_col-1])
                matrix[alice_row][alice_col - 1] = '*'
            elif matrix[alice_row][alice_col-1] == "R":
                matrix[alice_row][alice_col - 1] = '*'
                dies = True
                break
            alice_row = alice_row
            alice_col = alice_col - 1
        else:
            dies = True
            break
    if command == "up":
        matrix[alice_row][alice_col] = "*"
        if 0 <= alice_row-1 < size:
            if matrix[alice_row-1][alice_col] == ".":
                matrix[alice_row-1][alice_col] = '*'
            elif matrix[alice_row-1][alice_col].isdigit():
                tea += int(matrix[alice_row-1][alice_col])
                matrix[alice_row-1][alice_col] = '*'
            elif matrix[alice_row-1][alice_col] == "R":
                matrix[alice_row-1][alice_col] = '*'
                dies = True
                break
            alice_row = alice_row - 1
            alice_col = alice_col
        else:
            dies = True
            break
    if command == "down":
        matrix[alice_row][alice_col] = "*"
        if 0 <= alice_row+1 < size:
            if matrix[alice_row+1][alice_col] == ".":
                matrix[alice_row+1][alice_col] = '*'
            elif matrix[alice_row+1][alice_col].isdigit():
                tea += int(matrix[alice_row+1][alice_col])
                matrix[alice_row+1][alice_col] = '*'
            elif matrix[alice_row+1][alice_col] == "R":
                matrix[alice_row+1][alice_col] = '*'
                dies = True
                break
            alice_row = alice_row + 1
            alice_col = alice_col
        else:
            dies = True
            break

    if tea >= 10:
        wins = True
        break

    if dies:
        break

if dies:
    print("Alice didn't make it to the tea party.")
if wins:
    print(f"She did it! She went to the party.")
for row in matrix:
    print(*row, sep=' ')
