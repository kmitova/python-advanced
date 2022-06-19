size = 5
player_row = 0
player_col = 0
matrix = []
total_targets = 0
shot_targets = 0
shot_targets_placements = []
for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        element = data[col]
        if element == "A":
            player_row = row
            player_col = col
        elif element == 'x':
            total_targets += 1

n = int(input())

for i in range(n):
    # matrix[player_row][player_col] = '.'
    command_str = input()
    command = command_str.split()
    if command[0] == 'shoot':
        if command[1] == 'right':
            for j in range(player_col, size):
                if matrix[player_row][j] == 'x':
                    shot_targets += 1
                    shot_targets_placements.append([player_row, j])
                    matrix[player_row][j] = '.'
                    break
        elif command[1] == 'down':
            for j in range(player_row, size):
                if matrix[j][player_col] == 'x':
                    shot_targets += 1
                    shot_targets_placements.append([j, player_col])
                    matrix[j][player_col] = '.'
                    break
        elif command[1] == 'up':
            for j in range(player_row-1, -1, -1):
                if matrix[j][player_col] == 'x':
                    shot_targets += 1
                    shot_targets_placements.append([j, player_col])
                    matrix[j][player_col] = '.'
                    break

        elif command[1] == 'left':
            for j in range(player_col - 1, -1, -1):
                if matrix[player_row][j] == 'x':
                    shot_targets += 1
                    shot_targets_placements.append([player_row, j])
                    matrix[player_row][j] = '.'
                    break
    elif command[0] == 'move':
        steps = int(command[2])
        if command[1] == 'right':
            if player_col + steps < size:
                if matrix[player_row][player_col+steps] != 'x':
                    player_col = player_col + steps
        elif command[1] == 'left':
            if player_col - steps >= 0:
                if matrix[player_row][player_col-steps] != 'x':
                    player_col = player_col - steps
        elif command[1] == 'up':
            if player_row - steps >= 0:
                if matrix[player_row - steps][player_col] != 'x':
                    player_row = player_row - steps
        elif command[1] == 'down':
            if player_row + steps < size:
                if matrix[player_row + steps][player_col] != 'x':
                    player_row = player_row + steps
        matrix[player_row][player_col] = '.'
    if shot_targets == total_targets:
        break

if shot_targets == total_targets:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets - shot_targets} targets left.")

print(*shot_targets_placements, sep='\n')
