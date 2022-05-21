rows, cols = [int(el) for el in input().split()]

matrix = []

for i in range(rows):
    nums = [x for x in input().split()]
    matrix.append(nums)

command = input()
while not command == "END":
    data = command.split()
    if not len(data) == 5:
        print('Invalid input!')
    else:
        row1 = int(data[1])
        col1 = int(data[2])
        row2 = int(data[3])
        col2 = int(data[4])
        if not data[0] == "swap" or row1 >= len(matrix) or row2 >= len(matrix):
            print('Invalid input!')
        elif col1 >= len(matrix[row1]) or col2 >= len(matrix[row2]):
            print('Invalid input!')
        else:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for el in matrix:
                print(*el)
    command = input()
