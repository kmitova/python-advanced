size = 7
matrix = []
player1_points = 501
player2_points = 501
player1_turns = 0
player2_turns = 0
player1_wins = False
player2_wins = False

name1, name2 = input().split(', ')
for row in range(size):
    data = input().split(' ')

    matrix.append(data)

throw = 0

while True:
    # player one
    if throw % 2 == 0:
        player1_turns += 1
        info = input()
        info = info.replace("(", "")
        info = info.replace(")", "")
        coords = [int(x) for x in info.split(", ")]
        row = coords[0]
        col = coords[1]
        if row in range(size) and col in range(size):
            if matrix[row][col] == "T":
                sum_points = int(matrix[row][0]) + int(matrix[0][col]) + \
                             int(matrix[row][size - 1]) + \
                             int(matrix[size - 1][col])
                sum_points *= 3
                player1_points -= sum_points
            elif matrix[row][col] == "D":
                sum_points = int(matrix[row][0]) + int(matrix[0][col]) + \
                             int(matrix[row][size-1]) + \
                             int(matrix[size-1][col])
                sum_points *= 2
                player1_points -= sum_points
            elif matrix[row][col] == "B":
                player1_wins = True
                break
            else:
                player1_points -= int(matrix[row][col])
        if player1_points <= 0:
            player1_wins = True
            break
        # player 2 turn
    if not throw % 2 == 0:
        player2_turns += 1
        info = input()
        info = info.replace("(", "")
        info = info.replace(")", "")
        coords = [int(x) for x in info.split(", ")]
        row = coords[0]
        col = coords[1]
        if row in range(size) and col in range(size):
            if matrix[row][col] == "T":
                sum_points = int(matrix[row][0]) + int(matrix[0][col]) + \
                             int(matrix[row][size - 1]) + \
                             int(matrix[size - 1][col])
                sum_points *= 3
                player2_points -= sum_points
            elif matrix[row][col] == "D":
                sum_points = int(matrix[row][0]) + int(matrix[0][col]) + \
                             int(matrix[row][size - 1]) + \
                             int(matrix[size - 1][col])
                sum_points *= 2
                player2_points -= sum_points
            elif matrix[row][col] == "B":
                player2_wins = True
                break
            else:
                player2_points -= int(matrix[row][col])
        if player2_points <= 0:
            player2_wins = True
            break
    throw += 1

if player1_wins:
    print(f"{name1} won the game with {player1_turns} throws!")
if player2_wins:
    print(f"{name2} won the game with {player2_turns} throws!")
