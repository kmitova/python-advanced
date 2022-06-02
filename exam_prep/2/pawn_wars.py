size = 8
matrix = []
white_row = 0
white_col = 0
black_row = 0
black_col = 0
white_queen = False
white_captures = False
black_queen = False
black_captures = False
position = []
for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        element = data[col]
        if element == "w":
            white_row = row
            white_col = col
        if element == "b":
            black_row = row
            black_col = col

while True:
    # white moves
    matrix[white_row][white_col] = '-'
    if white_row - 1 == 0:
        white_queen = True
        position.append([white_row-1, white_col])
        break
    if white_row - 1 >= 0 and white_col-1 >= 0:
        if matrix[white_row-1][white_col-1] == 'b':
            position.append([white_row-1, white_col-1])
            white_captures = True
            break
    if white_row - 1 >= 0 and white_col + 1 < 8:
        if matrix[white_row-1][white_col+1] == 'b':
            position.append([white_row - 1, white_col + 1])
            white_captures = True
            break
    if white_row + 1 < 8 and white_col - 1 >= 0:
        if matrix[white_row+1][white_col-1] == 'b':
            position.append([white_row + 1, white_col - 1])
            white_captures = True
            break
    if white_row + 1 < 8 and white_col + 1 < 8:
        if matrix[white_row+1][white_col+1] == 'b':
            position.append([white_row + 1, white_col + 1])
            white_captures = True
            break
    white_row = white_row - 1
    matrix[white_row][white_col] = 'w'
    # black moves
    matrix[black_row][black_col] = '-'
    if black_row + 1 == 7:
        black_queen = True
        position.append([black_row + 1, black_col])
        break
    if black_row - 1 >= 0 and black_col - 1 >= 0:
        if matrix[black_row - 1][black_col - 1] == 'w':
            position.append([black_row - 1, black_col - 1])
            black_captures = True
            break
    if black_row - 1 >= 0 and black_col + 1 < 8:
        if matrix[black_row - 1][black_col + 1] == 'w':
            position.append([black_row - 1, black_col + 1])
            black_captures = True
            break
    if black_row + 1 < 8 and black_col - 1 >= 0:
        if matrix[black_row + 1][black_col - 1] == 'w':
            position.append([black_row + 1, black_col - 1])
            black_captures = True
            break
    if black_row + 1 < 8 and black_col + 1 < 8:
        if matrix[black_row + 1][black_col + 1] == 'w':
            position.append([black_row + 1, black_col + 1])
            black_captures = True
            break
    black_row = black_row + 1
    matrix[black_row][black_col] = 'b'

# print(position)

result = position[0][::-1]
# print(result)
point = ''
if result[0] == 0:
    point += 'a'
if result[0] == 1:
    point += 'b'
if result[0] == 2:
    point += 'c'
if result[0] == 3:
    point += 'd'
if result[0] == 4:
    point += 'e'
if result[0] == 5:
    point += 'f'
if result[0] == 6:
    point += 'g'
if result[0] == 7:
    point += 'h'


if result[1] == 0:
    point += '8'
if result[1] == 1:
    point += '7'
if result[1] == 2:
    point += '6'
if result[1] == 3:
    point += '5'
if result[1] == 4:
    point += '4'
if result[1] == 5:
    point += '3'
if result[1] == 6:
    point += '2'
if result[1] == 7:
    point += '1'
# print(point)
if white_queen:
    print(f"Game over! White pawn is promoted to a queen at {point}.")

if white_captures:
    print(f"Game over! White win, capture on {point}.")

if black_queen:
    print(f"Game over! Black pawn is promoted to a queen at {point}.")

if black_captures:
    print(f"Game over! Black win, capture on {point}.")
