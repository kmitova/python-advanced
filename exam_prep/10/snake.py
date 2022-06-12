size = int(input())
snake_row = 0
snake_col = 0
matrix = []
burrow1_row = 0
burrow1_col = 0
burrow2_row = 0
burrow2_col = 0
out_of_territory = False
enough_food = False

for row in range(size):
    data = list(input())
    matrix.append(data)
    for col in range(size):
        element = data[col]
        if element == "S":
            snake_row = row
            snake_col = col
        if element == "B":
            if burrow1_col == 0:
                burrow1_row = row
                burrow1_col = col
            else:
                burrow2_row = row
                burrow2_col = col
eaten = 0

while not out_of_territory:
    command = input()
    matrix[snake_row][snake_col] = "."
    if command == "right":
        if snake_col + 1 >= size:
            out_of_territory = True
        else:
            snake_col = snake_col + 1
            if matrix[snake_row][snake_col] == "*":
                eaten += 1
                matrix[snake_row][snake_col] = '.'
            elif matrix[snake_row][snake_col] == "B":
                if snake_row == burrow1_row and snake_col == burrow1_col:
                    matrix[snake_row][snake_col] = '.'
                    snake_row = burrow2_row
                    snake_col = burrow2_col
                elif snake_row == burrow2_row and snake_col == burrow2_col:
                    matrix[snake_row][snake_col] = '.'
                    snake_row = burrow1_row
                    snake_col = burrow1_col
            else:
                matrix[snake_row][snake_col] = '.'
    if command == "left":
        if snake_col - 1 < 0:
            out_of_territory = True
        else:
            snake_col = snake_col - 1
            if matrix[snake_row][snake_col] == "*":
                eaten += 1
                matrix[snake_row][snake_col] = '.'
            elif matrix[snake_row][snake_col] == "B":
                if snake_row == burrow1_row and snake_col == burrow1_col:
                    matrix[snake_row][snake_col] = '.'
                    snake_row = burrow2_row
                    snake_col = burrow2_col
                elif snake_row == burrow2_row and snake_col == burrow2_col:
                    matrix[snake_row][snake_col] = '.'
                    snake_row = burrow1_row
                    snake_col = burrow1_col
            else:
                matrix[snake_row][snake_col] = '.'
    if command == "down":
        if snake_row + 1 >= size:
            out_of_territory = True
        else:
            snake_row = snake_row + 1
            if matrix[snake_row][snake_col] == "*":
                eaten += 1
                matrix[snake_row][snake_col] = '.'
            elif matrix[snake_row][snake_col] == "B":
                if snake_row == burrow1_row and snake_col == burrow1_col:
                    matrix[snake_row][snake_col] = '.'
                    snake_row = burrow2_row
                    snake_col = burrow2_col
                elif snake_row == burrow2_row and snake_col == burrow2_col:
                    matrix[snake_row][snake_col] = '.'
                    snake_row = burrow1_row
                    snake_col = burrow1_col
            else:
                matrix[snake_row][snake_col] = '.'
    if command == "up":
        if snake_row - 1 < 0:
            out_of_territory = True
        else:
            snake_row = snake_row - 1
            if matrix[snake_row][snake_col] == "*":
                eaten += 1
                matrix[snake_row][snake_col] = '.'
            elif matrix[snake_row][snake_col] == "B":
                if snake_row == burrow1_row and snake_col == burrow1_col:
                    matrix[snake_row][snake_col] = '.'
                    snake_row = burrow2_row
                    snake_col = burrow2_col
                elif snake_row == burrow2_row and snake_col == burrow2_col:
                    matrix[snake_row][snake_col] = '.'
                    snake_row = burrow1_row
                    snake_col = burrow1_col
            else:
                matrix[snake_row][snake_col] = '.'
    matrix[snake_row][snake_col] = "S"
    if eaten >= 10:
        enough_food = True
        break

if out_of_territory:
    print("Game over!")
    print(f"Food eaten: {eaten}")
    matrix[snake_row][snake_col] = "."

if enough_food:
    print("You won! You fed the snake.")
    print(f"Food eaten: {eaten}")
    matrix[snake_row][snake_col] = "S"

for row in matrix:
    print(''.join(row))


