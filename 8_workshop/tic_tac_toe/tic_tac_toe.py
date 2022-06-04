from math import ceil


def setup():
    global player_one, player_two
    player_one_name = input("Player one name: ")
    player_two_name = input("Player two name: ")
    player_one_sign = input(f"{player_one_name} would you like to play with X or O? ")
    player_two_sign = 'X' if player_one_sign == 'O' else 'O'
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print(f"{player_one_name} starts first!")


def play(current, board):
    choice = int(input(f"{current[0]} choose a free position [1-9]: "))
    row = ceil(choice / 3) - 1
    col = choice % 3 - 1
    board[row][col] = current[1]
    draw_board(board)
    check_if_won(current, board)


def draw_board(board):
    for row in board:
        print('| ', end='')
        print(' | '.join([str(x) for x in row]), end='')
        print(' |')


def check_if_won(current, board):
    global loop
    first_row = all([x == current[1] for x in board[0]])
    second_row = all([x == current[1] for x in board[1]])
    third_row = all([x == current[1] for x in board[2]])
    first_column = all(x == current[1] for x in [board[0][0], board[1][0], board[2][0]])
    second_column = all(x == current[1] for x in [board[0][1], board[1][1], board[2][1]])
    third_column = all(x == current[1] for x in [board[0][2], board[1][2], board[2][2]])
    first_diagonal = all(x == current[1] for x in [board[0][0], board[1][1], board[2][2]])
    second_diagonal = all(x == current[1] for x in [board[2][0], board[1][1], board[0][2]])

    if any([first_row, second_row, third_row, first_column, second_column, third_column,
            first_diagonal, second_diagonal]):
        print(f"{current[0]} won the game!")
        loop = False


player_one = None
player_two = None
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
setup()
current = player_one
other = player_two
loop = True
while loop:
    play(current, board)
    current, other = other, current
