size = int(input())

matrix = []
for row in range(size):
    data = list(input())
    matrix.append(data)
    # for col in range(size):
    #     element = data[col]

removed = 0


def is_knight(row, col, matrix):
    return matrix[row][col] == "K"


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_attack_counter(row, col, matrix):
    # All cases:
    result = 0
    # row, col
    # row -2 , col -1
    if is_inside(row-2, col-1, len(matrix)) and is_knight(row-2, col-1, matrix):
        result += 1
    # row -2 , col +1
    if is_inside(row-2, col+1, len(matrix)) and is_knight(row-2, col+1, matrix):
        result += 1
    # row -1 , col -2
    if is_inside(row - 1, col -2, len(matrix)) and is_knight(row - 1, col -2, matrix):
        result += 1
    # row -1 , col +2
    if is_inside(row - 1, col +2, len(matrix)) and is_knight(row - 1, col + 2, matrix):
        result += 1
    # row +2 , col -1
    if is_inside(row + 2, col - 1, len(matrix)) and is_knight(row + 2, col - 1, matrix):
        result += 1
    # row +2 , col +1
    if is_inside(row + 2, col + 1, len(matrix)) and is_knight(row + 2, col + 1, matrix):
        result += 1
    # row +1 , col -2
    if is_inside(row +1, col -2, len(matrix)) and is_knight(row +1, col -2, matrix):
        result += 1
    # row +1 , col +2
    if is_inside(row +1, col + 2, len(matrix)) and is_knight(row +1, col +2, matrix):
        result += 1
    return result


while True:
    table = {}
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == '0':
                continue
            counter = get_attack_counter(row, col, matrix)
            if counter:
                table[(row, col)] = counter
    if len(table) == 0:
        break

    best_counter = 0
    knight_row, knight_col = 0, 0

    for coords, counter in table.items():
        if counter > best_counter:
            best_counter = counter
            knight_row = coords[0]
            knight_col = coords[1]
    matrix[knight_row][knight_col] = '0'
    removed += 1

print(removed)
