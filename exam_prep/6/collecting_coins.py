size = int(input())
player_row = 0
player_col = 0
matrix = []
coins = 0
wins = False
loses = False
path = []

for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        element = data[col]
        if element == "P":
            player_row = row
            player_col = col

path.append([player_row, player_col])

while True:
    command = input()
    matrix[player_row][player_col] = '-'
    if command == "right":
        if player_col + 1 < size:
            player_col = player_col + 1
            player_row = player_row
            if matrix[player_row][player_col] == "X":
                loses = True
                path.append([player_row, player_col])
                break
            if matrix[player_row][player_col] == '-':
                path.append([player_row, player_col])
            else:
                current_coins = int(matrix[player_row][player_col])
                matrix[player_row][player_col] = '-'
                coins += current_coins
                path.append([player_row, player_col])

        else:
            player_col = 0
            player_row = player_row
            if matrix[player_row][player_col] == "X":
                loses = True
                path.append([player_row, player_col])
                break
            if matrix[player_row][player_col] == '-':
                path.append([player_row, player_col])
            else:
                current_coins = int(matrix[player_row][player_col])
                matrix[player_row][player_col] = '-'
                coins += current_coins
                path.append([player_row, player_col])
    elif command == "left":
        if player_col - 1 >= 0:
            player_col = player_col - 1
            player_row = player_row
            if matrix[player_row][player_col] == "X":
                loses = True
                path.append([player_row, player_col])
                break
            if matrix[player_row][player_col] == '-':
                path.append([player_row, player_col])
            else:
                current_coins = int(matrix[player_row][player_col])
                matrix[player_row][player_col] = '-'
                coins += current_coins
                path.append([player_row, player_col])

        else:
            player_col = size - 1
            player_row = player_row
            if matrix[player_row][player_col] == "X":
                loses = True
                path.append([player_row, player_col])
                break
            if matrix[player_row][player_col] == '-':
                path.append([player_row, player_col])
            else:
                current_coins = int(matrix[player_row][player_col])
                matrix[player_row][player_col] = '-'
                coins += current_coins
                path.append([player_row, player_col])
    elif command == "down":
        if player_row + 1 < size:
            player_col = player_col
            player_row = player_row + 1
            if matrix[player_row][player_col] == "X":
                loses = True
                path.append([player_row, player_col])
                break
            if matrix[player_row][player_col] == '-':
                path.append([player_row, player_col])
            else:
                current_coins = int(matrix[player_row][player_col])
                matrix[player_row][player_col] = '-'
                coins += current_coins
                path.append([player_row, player_col])

        else:
            player_col = player_col
            player_row = 0
            if matrix[player_row][player_col] == "X":
                loses = True
                path.append([player_row, player_col])
                break
            if matrix[player_row][player_col] == '-':
                path.append([player_row, player_col])
            else:
                current_coins = int(matrix[player_row][player_col])
                matrix[player_row][player_col] = '-'
                coins += current_coins
                path.append([player_row, player_col])

    elif command == "up":
        if player_row - 1 >= 0:
            player_col = player_col
            player_row = player_row - 1
            if matrix[player_row][player_col] == "X":
                loses = True
                path.append([player_row, player_col])
                break
            if matrix[player_row][player_col] == '-':
                path.append([player_row, player_col])
            else:
                current_coins = int(matrix[player_row][player_col])
                matrix[player_row][player_col] = '-'
                coins += current_coins
                path.append([player_row, player_col])

        else:
            player_col = player_col
            player_row = size - 1
            if matrix[player_row][player_col] == "X":
                loses = True
                path.append([player_row, player_col])
                break
            if matrix[player_row][player_col] == '-':
                path.append([player_row, player_col])
            else:
                current_coins = int(matrix[player_row][player_col])
                matrix[player_row][player_col] = '-'
                coins += current_coins
                path.append([player_row, player_col])

    if coins >= 100:
        wins = True
        break

if loses:
    print(f"Game over! You've collected {int(coins/2)} coins.")
if wins:
    print(f"You won! You've collected {coins} coins.")
print("Your path:")
print(*path, sep='\n')
