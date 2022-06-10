size = 8
possible_queens = []
matrix = []
king_row = 0
king_col = 0

for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        element = data[col]
        if element == "E":
            king_row = row
            king_col = col

current_row = 0
current_col = 0
for row in matrix:
    current_col = 0
    for el in row:

        if el == "Q":
            for ind in range(current_col+1, size):
                if matrix[current_row][ind] == "Q":
                    break
                elif matrix[current_row][ind] == "K":
                    possible_queens.append([current_row, current_col])
                    break
            # left
            for ind in range(current_col-1, -1, -1):
                if matrix[current_row][ind] == "Q":
                    break
                elif matrix[current_row][ind] == "K":
                    possible_queens.append([current_row, current_col])
                    break
        #     down
            for ind in range(current_row+1, size):
                if matrix[ind][current_col] == "Q":
                    break
                elif matrix[ind][current_col] == "K":
                    possible_queens.append([current_row, current_col])
                    break
        # up
            for ind in range(current_row - 1, -1, -1):
                if matrix[ind][current_col] == "Q":
                    break
                elif matrix[ind][current_col] == "K":
                    possible_queens.append([current_row, current_col])
                    break
        # diagonal down right
            for i in range(1, size):
                if i + current_row >= size or i + current_col >= size:
                    break
                if matrix[current_row+i][current_col+i] == "Q":
                    break
                elif matrix[current_row+i][current_col+i] == "K":
                    possible_queens.append([current_row, current_col])
                    break
        # diagonal down left
            for i in range(1, size):
                if i + current_row >= size or current_col - i < 0:
                    break
                if matrix[current_row + i][current_col - i] == "Q":
                    break
                elif matrix[current_row + i][current_col - i] == "K":
                    possible_queens.append([current_row, current_col])
                    break
        # diagonal up right
            for i in range(1, size):
                if current_row - i < 0 or current_col + i >= size:
                    break
                if matrix[current_row - i][current_col + i] == "Q":
                    break
                elif matrix[current_row - i][current_col + i] == "K":
                    possible_queens.append([current_row, current_col])
                    break
        # diagonal up left
            for i in range(1, size):
                if current_row - i < 0 or current_col - i < 0:
                    break
                if matrix[current_row - i][current_col - i] == "Q":
                    break
                elif matrix[current_row - i][current_col - i] == "K":
                    possible_queens.append([current_row, current_col])
                    break
        current_col += 1

    current_row += 1

if len(possible_queens) == 0:
    print("The king is safe!")
else:

    print(*possible_queens, sep='\n')
