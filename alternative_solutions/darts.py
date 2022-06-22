size = 7
matrix = []
player1_score = 501
player2_score = 501
player1_throws = 0
player2_throws = 0
player2_wins = False
player1_wins = False
player1_turn = False
player2_turn = False
player1, player2 = input().split(', ')

for row in range(size):
    data = input().split()
    matrix.append(data)

count = 0
while True:
    throw = input()
    throw = throw.replace('(', '')
    throw = throw.replace(')', '')
    coords = throw.split(', ')
    row = int(coords[0])
    col = int(coords[1])
    count += 1
    if count % 2 != 0:
        player1_throws += 1
        if row in range(0, size) and col in range(0, size):
            if matrix[row][col] == 'D':
                value = (int(matrix[0][col]) + int(matrix[row][0]) +
                        int(matrix[row][size-1]) + int(matrix[size-1][col])) * 2
                player1_score -= value
            elif matrix[row][col] == 'T':
                value = (int(matrix[0][col]) + int(matrix[row][0]) +
                         int(matrix[row][size - 1]) + int(matrix[size - 1][col])) * 3
                player1_score -= value
            elif matrix[row][col] == 'B':
                player1_wins = True
                break
            else:
                player1_score -= int(matrix[row][col])
        if player1_score <= 0:
            player1_wins = True
            break
    else:
        player2_throws += 1
        if row in range(0, size) and col in range(0, size):
            if matrix[row][col] == 'D':
                value = (int(matrix[0][col]) + int(matrix[row][0]) +
                        int(matrix[row][size-1]) + int(matrix[size-1][col])) * 2
                player2_score -= value
            elif matrix[row][col] == 'T':
                value = (int(matrix[0][col]) + int(matrix[row][0]) +
                         int(matrix[row][size - 1]) + int(matrix[size - 1][col])) * 3
                player2_score -= value
            elif matrix[row][col] == 'B':
                player2_wins = True
                break
            else:
                player2_score -= int(matrix[row][col])
        if player2_score <= 0:
            player2_wins = True
            break


if player1_wins:
    print(f"{player1} won the game with {player1_throws} throws!")

if player2_wins:
    print(f"{player2} won the game with {player2_throws} throws!")
