# description and solution in matrix exercise 2


def is_valid(num, size):
    return 0 <= num < size


n = int(input())
bunny_pos = ()
directions = {'up': (-1, 0),
              'right': (0, 1),
              'down': (1, 0),
              'left': (0, -1)}

field = []
for row in range(n):
    line = input().split()
    if 'B' in line:
        bunny_pos = (row, line.index('B'))
    field.append(line)

best_sum = -9999999999999
best_dir = ''
for direction in directions:
    current_sum = 0
    row = bunny_pos[0]
    col = bunny_pos[1]
    if not is_valid(row + directions[direction][0], n) or not is_valid(col + directions[direction][1], n):
        continue
    while is_valid(row, n) and is_valid(col, n):
        current_cell = field[row][col]
        if current_cell != 'B' and current_cell != 'X':
            current_sum += int(current_cell)
        elif current_cell == 'X':
            break
        row += directions[direction][0]
        col += directions[direction][1]
    if current_sum > best_sum:
        best_sum = current_sum
        best_dir = direction

print(best_dir)
row = bunny_pos[0] + directions[best_dir][0]
col = bunny_pos[1] + directions[best_dir][1]
while is_valid(row, n) and is_valid(col, n):
    if field[row][col] == 'X':
        break
    print([row, col])
    row += directions[best_dir][0]
    col += directions[best_dir][1]
print(best_sum)
