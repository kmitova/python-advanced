def get_next_position(command, row, col):
    if command == 'up':
        return row - 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1
    if command == 'down':
        return row + 1, col


size = int(input())
commands = input().split()
matrix = []

game_over = False

miner_row = 0
miner_col = 0
total_coal = 0

for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        element = data[col]
        if element == 's':
            miner_row = row
            miner_col = col
        elif element == 'c':
            total_coal += 1


for command in commands:
    next_row, next_col = get_next_position(command, miner_row, miner_col)

    if 0 <= next_row < size and 0 <= next_col < size:
        miner_row, miner_col = next_row, next_col
        if matrix[miner_row][miner_col] == 'c':
            matrix[miner_row][miner_col] = '*'
            total_coal -= 1
            if total_coal == 0:
                break
        elif matrix[miner_row][miner_col] == 'e':
            game_over = True
            break

if total_coal == 0:
    print(f"You collected all coal! ({miner_row}, {miner_col})")

elif game_over:
    print(f"Game over! ({miner_row}, {miner_col})")

else:
    print(f"{total_coal} pieces of coal left. ({miner_row}, {miner_col})")
