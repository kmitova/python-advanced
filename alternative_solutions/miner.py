size = int(input())

matrix = []

commands = input().split()
miner_row = 0
miner_col = 0
all_coal = 0
coal = 0
dies = False
for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        element = data[col]
        if element == "s":
            miner_row = row
            miner_col = col
        if element == 'c':
            all_coal += 1

for direction in commands:
    current_position = matrix[miner_row][miner_col]
    matrix[miner_row][miner_col] = '*'
    # right
    if direction == 'right':
        if miner_col + 1 < size:
            miner_col = miner_col + 1
            if matrix[miner_row][miner_col] == 'c':
                coal += 1
                matrix[miner_row][miner_col] = '*'
            if matrix[miner_row][miner_col] == 'e':
                dies = True
    # left
    if direction == 'left':
        if miner_col - 1 >= 0:
            miner_col = miner_col - 1
            if matrix[miner_row][miner_col] == 'c':
                coal += 1
                matrix[miner_row][miner_col] = '*'
            if matrix[miner_row][miner_col] == 'e':
                dies = True
    # down
    if direction == 'down':
        if miner_row + 1 < size:
            miner_row = miner_row + 1
            if matrix[miner_row][miner_col] == 'c':
                coal += 1
                matrix[miner_row][miner_col] = '*'
            if matrix[miner_row][miner_col] == 'e':
                dies = True
    # up
    if direction == 'up':
        if miner_row - 1 >= 0:
            miner_row = miner_row - 1
            if matrix[miner_row][miner_col] == 'c':
                coal += 1
                matrix[miner_row][miner_col] = '*'
            if matrix[miner_row][miner_col] == 'e':
                dies = True
    if dies:
        break
    if coal == all_coal:
        break

if dies:
    print(f"Game over! ({miner_row}, {miner_col})")
elif all_coal == coal:
    print(f"You collected all coal! ({miner_row}, {miner_col})")
else:
    print(f"{all_coal-coal} pieces of coal left. ({miner_row}, {miner_col})")
