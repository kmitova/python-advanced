size = 5
matrix = []
player_row = 0
player_col = 0
targets = 0
targets_field = []

for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        elem = data[col]
        if elem == 'A':
            player_row = row
            player_col = col
        if elem == 'x':
            targets += 1

all = targets

commands = int(input())
for i in range(commands):
    command = input().split()
    if len(command) == 3:
        direction = command[1]
        steps = int(command[2])

        # RIGHT
        if direction == "right":
            if 0 <= player_col+steps < size and matrix[player_row][player_col+steps] != 'x':
                matrix[player_row][player_col] = '.'
                player_row = player_row
                player_col = player_col + steps
        # LEFT
        elif direction == 'left':
            if 0 <= player_col-steps < size and matrix[player_row][player_col-steps] != 'x':
                matrix[player_row][player_col] = '.'
                player_row = player_row
                player_col = player_col - steps
        # DOWN
        elif direction == 'down':
            if 0 <= player_row+steps < size and matrix[player_row+steps][player_col] != 'x':
                matrix[player_row][player_col] = '.'
                player_row = player_row + steps
                player_col = player_col
        # UP
        elif direction == 'up':
            if 0 <= player_row-steps < size and matrix[player_row-steps][player_col] != 'x':
                matrix[player_row][player_col] = '.'
                player_row = player_row - steps
                player_col = player_col

    elif len(command) == 2:
        direction = command[1]
        # RIGHT
        if direction == 'right':
            for ind in range(player_col+1, size):
                if matrix[player_row][ind] == 'x':
                    matrix[player_row][ind] = '.'
                    targets_field.append([player_row, ind])
                    targets -= 1
                    break
        # LEFT
        if direction == 'left':
            for ind in range(player_col-1, -1, -1):
                if matrix[player_row][ind] == 'x':
                    matrix[player_row][ind] = '.'
                    targets_field.append([player_row, ind])
                    targets -= 1
                    break
        # DOWN
        if direction == 'down':
            for ind in range(player_row+1, size):
                if matrix[ind][player_col] == 'x':
                    matrix[ind][player_col] = '.'
                    targets_field.append([ind, player_col])
                    targets -= 1
                    break
        # UP
        if direction == 'up':
            for ind in range(player_row-1, -1, -1):
                if matrix[ind][player_col] == 'x':
                    matrix[ind][player_col] = '.'
                    targets_field.append([ind, player_col])
                    targets -= 1
                    break
    if targets == 0:
        break

if targets == 0:
    print(f"Training completed! All {all} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")
for el in targets_field:
    print(el)
