size = int(input())
matrix = []
player_row = 0
player_col = 0
wins = False
loses = False
points = 0
for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        element = data[col]
        if element == "P":
            player_row = row
            player_col = col

# for row in matrix:
#     print(*row)
path = [[player_row, player_col]]
while True:
    command = input()
    matrix[player_row][player_col] = 0
    if command == 'right':
        if player_col + 1 < size:
            player_col = player_col + 1
        else:
            player_col = 0
        if matrix[player_row][player_col] == 'X':
            loses = True
        else:
            points += int(matrix[player_row][player_col])
    if command == 'left':
        if player_col - 1 >= 0:
            player_col = player_col - 1
        else:
            player_col = size - 1
        if matrix[player_row][player_col] == 'X':
            loses = True
        else:
            points += int(matrix[player_row][player_col])
    if command == 'down':
        if player_row + 1 < size:
            player_row = player_row + 1
        else:
            player_row = 0
        if matrix[player_row][player_col] == 'X':
            loses = True
        else:
            points += int(matrix[player_row][player_col])
    if command == 'up':
        if player_row - 1 >= 0:
            player_row = player_row - 1
        else:
            player_row = size - 1
        if matrix[player_row][player_col] == 'X':
            loses = True
        else:
            points += int(matrix[player_row][player_col])
    path.append([player_row, player_col])
    if loses:
        break
    if points >= 100:
        wins = True
        break

if wins:
    print(f"You won! You've collected {points} coins.")
if loses:
    points /= 2
    print(f"Game over! You've collected {int(points)} coins.")
print("Your path:")
print(*path, sep='\n')