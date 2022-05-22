def move_up(row, col):
    return row-1, col


def move_down(row, col):
    return row+1, col


def move_right(row, col):
    return row, col+1


def move_left(row, col):
    return row, col-1


size = int(input())
matrix = []
bunny_row = 0
bunny_col = 0

for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        elem = data[col]
        if elem == 'B':
            bunny_row = row
            bunny_col = col

directions = {
    'up': move_up,
    'down': move_down,
    'right': move_right,
    'left': move_left
}

best_score = float('-inf')  # - infinity, similar ot -sys.maxsize
best_dir = ''
best_path = []
for direction, step in directions.items():
    current_row, current_col = bunny_row, bunny_col
    current_score = 0
    path = []
    while True:
        current_row, current_col = step(current_row, current_col)
        if current_row < 0 or current_col < 0 or current_row >= size or current_col >= size:
            break
        if matrix[current_row][current_col] == 'X':
            break
        path.append([current_row, current_col])
        current_score += int(matrix[current_row][current_col])
    if current_score > best_score and path:
        best_score = current_score
        best_dir = direction
        best_path = path

print(best_dir)
for step in best_path:
    print(step)
print(best_score)
