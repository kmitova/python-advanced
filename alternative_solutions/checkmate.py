size = 8
matrix = []
possible = []

for row in range(size):
    data = input().split()
    matrix.append(data)

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'Q':
            # right
            for i in range(col+1, size):
                if matrix[row][i] == 'Q':
                    break
                elif matrix[row][i] == 'K':
                    possible.append([row, col])
            # left
            for i in range(col-1, -1, -1):
                if matrix[row][i] == 'Q':
                    break
                elif matrix[row][i] == 'K':
                    possible.append([row, col])
            # up
            for i in range(row-1, -1, -1):
                if matrix[i][col] == 'Q':
                    break
                elif matrix[i][col] == 'K':
                    possible.append([row, col])
            # down
            for i in range(row+1, size):
                if matrix[i][col] == 'Q':
                    break
                elif matrix[i][col] == 'K':
                    possible.append([row, col])
            # right down
            for i in range(1, size):
                if i + row >= size or i + col >= size:
                    break
                if matrix[row+i][col+i] == "Q":
                    break
                elif matrix[row+i][col+i] == "K":
                    possible.append([row, col])
                    break
            # up left
            for i in range(1, size):
                if row - i < 0 or col - i < 0:
                    break
                if matrix[row - i][col - i] == "Q":
                    break
                elif matrix[row - i][col - i] == "K":
                    possible.append([row, col])
                    break
            # down left
            for i in range(1, size):
                if i + row >= size or col - i < 0:
                    break
                if matrix[row + i][col - i] == "Q":
                    break
                elif matrix[row + i][col - i] == "K":
                    possible.append([row, col])
                    break
            # up right
            for i in range(1, size):
                if row - i < 0 or col + i >= size:
                    break
                if matrix[row - i][col + i] == "Q":
                    break
                elif matrix[row - i][col + i] == "K":
                    possible.append([row, col])
                    break

if len(possible) == 0:
    print("The king is safe!")
else:
    print(*possible, sep='\n')