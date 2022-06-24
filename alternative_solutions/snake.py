size = int(input())
snake_row = 0
snake_col = 0
matrix = []
out_of_field = False
food = 0

for row in range(size):
    data = list(input())
    matrix.append(data)
    for col in range(size):
        element = data[col]
        if element == "S":
            snake_row = row
            snake_col = col

while True:
    command = input()
    matrix[snake_row][snake_col] = '.'
    if command == 'right':
        if snake_col + 1 < size:
            snake_col = snake_col + 1
            if matrix[snake_row][snake_col] == '*':
                matrix[snake_row][snake_col] = '.'
                food += 1
            if matrix[snake_row][snake_col] == 'B':
                matrix[snake_row][snake_col] = '.'
                for row in range(len(matrix)):
                    for col in range(len(matrix)):
                        if col != snake_col:
                            if matrix[row][col] == 'B':
                                snake_col = col
                                snake_row = row
        else:
            out_of_field = True
    if command == 'left':
        if snake_col - 1 >= 0:
            snake_col = snake_col - 1
            if matrix[snake_row][snake_col] == '*':
                matrix[snake_row][snake_col] = '.'
                food += 1
            if matrix[snake_row][snake_col] == 'B':
                matrix[snake_row][snake_col] = '.'
                for row in range(len(matrix)):
                    for col in range(len(matrix)):
                        if col != snake_col:
                            if matrix[row][col] == 'B':
                                snake_col = col
                                snake_row = row
        else:
            out_of_field = True
    if command == 'up':
        if snake_row - 1 >= 0:
            snake_row = snake_row - 1
            if matrix[snake_row][snake_col] == '*':
                matrix[snake_row][snake_col] = '.'
                food += 1
            if matrix[snake_row][snake_col] == 'B':
                matrix[snake_row][snake_col] = '.'
                for row in range(len(matrix)):
                    for col in range(len(matrix)):
                        if row != snake_row:
                            if matrix[row][col] == 'B':
                                snake_col = col
                                snake_row = row
        else:
            out_of_field = True
    if command == 'down':
        if snake_row + 1 < size:
            snake_row = snake_row + 1
            if matrix[snake_row][snake_col] == '*':
                food += 1
                matrix[snake_row][snake_col] = '.'
            if matrix[snake_row][snake_col] == 'B':
                matrix[snake_row][snake_col] = '.'
                for row in range(len(matrix)):
                    for col in range(len(matrix)):
                        if row != snake_row:
                            if matrix[row][col] == 'B':
                                snake_col = col
                                snake_row = row
        else:
            out_of_field = True

    if food == 10:
        print("You won! You fed the snake.")
        matrix[snake_row][snake_col] = 'S'
        break
    if out_of_field:
        print("Game over!")
        break
print(f"Food eaten: {food}")

for row in matrix:
    print(''.join(row))

