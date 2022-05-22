presents = int(input())
size = int(input())
matrix = []
nice = 0
nice_given = 0
santa_row = 0
santa_col = 0
no_presents = False
for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        elem = data[col]
        if elem == 'S':
            santa_row = row
            santa_col = col
        if elem == 'V':
            nice += 1

total_nice = nice

command = input()
while not command == "Christmas morning":
    if command == 'up':
        if 0 <= santa_row - 1 < size:
            matrix[santa_row][santa_col] = '-'
            if matrix[santa_row-1][santa_col] == 'V':
                nice -= 1
                presents -= 1
                matrix[santa_row - 1][santa_col] = '-'
            elif matrix[santa_row-1][santa_col] == 'X':
                matrix[santa_row - 1][santa_col] = '-'
            elif matrix[santa_row-1][santa_col] == 'C':
                matrix[santa_row - 1][santa_col] = '-'
                if not matrix[santa_row-2][santa_col] == '-':
                    if matrix[santa_row-2][santa_col] == 'V':
                        nice -= 1
                    presents -= 1
                    matrix[santa_row - 2][santa_col] = '-'

                if not matrix[santa_row-1][santa_col-1] == '-':
                    if matrix[santa_row-1][santa_col-1] == 'V':
                        nice -= 1
                    presents -= 1
                    matrix[santa_row - 1][santa_col - 1] = '-'
                if not matrix[santa_row-1][santa_col+1] == '-':
                    if matrix[santa_row-1][santa_col+1] == 'V':
                        nice -= 1
                    presents -= 1
                    matrix[santa_row -1][santa_col + 1] = '-'

            santa_row = santa_row - 1
            santa_col = santa_col
    elif command == 'down':
        if 0 <= santa_row + 1 < size:
            matrix[santa_row][santa_col] = '-'
            if matrix[santa_row + 1][santa_col] == 'V':
                nice -= 1
                presents -= 1
                matrix[santa_row + 1][santa_col] = '-'
            elif matrix[santa_row + 1][santa_col] == 'X':
                matrix[santa_row + 1][santa_col] = '-'
            elif matrix[santa_row + 1][santa_col] == 'C':
                matrix[santa_row + 1][santa_col] = '-'
                if not matrix[santa_row + 2][santa_col] == '-':
                    if matrix[santa_row + 2][santa_col] == 'V':
                        nice -= 1
                    presents -= 1
                    matrix[santa_row + 2][santa_col] = '-'

                if not matrix[santa_row + 1][santa_col - 1] == '-':
                    if matrix[santa_row + 1][santa_col - 1] == 'V':
                        nice-= 1
                    presents -= 1
                    matrix[santa_row + 1][santa_col - 1] = '-'
                if not matrix[santa_row + 1][santa_col + 1] == '-':
                    if matrix[santa_row + 1][santa_col + 1] == 'V':
                        nice-= 1
                    presents -= 1
                    matrix[santa_row + 1][santa_col + 1] = '-'
        santa_row = santa_row + 1
        santa_col = santa_col
    elif command == 'left':
        if 0 <= santa_col - 1 < size:
            matrix[santa_row][santa_col] = '-'
            if matrix[santa_row][santa_col-1] == 'V':
                nice-= 1
                presents -= 1
                matrix[santa_row][santa_col - 1] = '-'
            elif matrix[santa_row][santa_col-1] == 'X':
                matrix[santa_row][santa_col-1] = '-'
            elif matrix[santa_row][santa_col-1] == 'C':
                matrix[santa_row][santa_col-1] = '-'
                if not matrix[santa_row - 1][santa_col -1] == '-':
                    if matrix[santa_row - 1][santa_col -1] == 'V':
                        nice-= 1
                    presents -= 1
                    matrix[santa_row - 1][santa_col-1] = '-'

                if not matrix[santa_row][santa_col -2] == '-':
                    if matrix[santa_row][santa_col - 2] == 'V':
                        nice-= 1
                    presents -= 1
                    matrix[santa_row][santa_col - 2] = '-'
                if not matrix[santa_row + 1][santa_col - 1] == '-':
                    if matrix[santa_row + 1][santa_col - 1] == 'V':
                        nice-= 1
                    presents -= 1
                    matrix[santa_row + 1][santa_col - 1] = '-'
        santa_col = santa_col - 1
        santa_row = santa_row
    elif command == 'right':
        if 0 <= santa_col + 1 < size:
            matrix[santa_row][santa_col] = '-'
            if matrix[santa_row][santa_col+1] == 'V':
                nice-= 1
                presents -= 1
                matrix[santa_row][santa_col + 1] = '-'
            elif matrix[santa_row][santa_col+1] == 'X':
                matrix[santa_row][santa_col+1] = '-'
            elif matrix[santa_row][santa_col+1] == 'C':
                matrix[santa_row][santa_col + 1] = '-'
                if not matrix[santa_row - 1][santa_col + 1] == '-':
                    if matrix[santa_row - 1][santa_col + 1] == 'V':
                        nice -= 1
                    presents -= 1
                    matrix[santa_row - 1][santa_col + 1] = '-'

                if not matrix[santa_row][santa_col + 2] == '-':
                    if matrix[santa_row][santa_col + 2] == 'V':
                        nice -= 1
                    presents -= 1
                    matrix[santa_row][santa_col + 2] = '-'
                if not matrix[santa_row + 1][santa_col + 1] == '-':
                    if matrix[santa_row + 1][santa_col + 1] == 'V':
                        nice -= 1
                    presents -= 1
                    matrix[santa_row + 1][santa_col + 1] = '-'
        santa_col = santa_col + 1
        santa_row = santa_row
    if presents == 0:
        no_presents = True
        break
    command = input()

# diff = total_nice - nice

matrix[santa_row][santa_col] = 'S'


if no_presents and nice > 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row, sep=" ")

if nice == 0:
    print(f"Good job, Santa! {total_nice} happy nice kid/s.")
else:
    print(f"No presents for {nice} nice kid/s.")
