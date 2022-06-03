'''
- create matrix
- print matrix
- read column choice from input
- verify player choice (1 or 2) - if not, choose again
- place player choice on board - check if there is space in column
- define winning conditions
'''


class InvalidColError(Exception):
    pass


class FullColumnError(Exception):
    pass


# print matrix
def print_matrix(ma):
    for el in ma:
        print(el)


# validate choice
def validate_col_choice(selected_col_num, max_col_index):
    if not (0 <= selected_col_num <= max_col_index):
        raise InvalidColError


def place_player_choice(ma, selected_col_index, player_num):
    rows = len(ma)
    for row_ind in range(rows - 1, -1, -1):
        current_element = ma[row_ind][selected_col_index]
        if current_element == 0:
            ma[row_ind][selected_col_index] = player_num
            return row_ind, selected_col_index
    raise FullColumnError


def check_spot(ma, row, col, player_num):
    if col < 0 or row < 0:
        return False
    try:
        if ma[row][col] == player_num:
            return True
    except IndexError:
        return False
    return False


def is_winner(ma, row, col, player_num, slots_count=4):
    is_right = all([check_spot(ma, row, col+ind, player_num) for ind in range(slots_count)])
    is_left = all([check_spot(ma, row, col-ind, player_num) for ind in range(slots_count)])
    is_up = all([check_spot(ma, row - ind, col, player_num) for ind in range(slots_count)])
    is_down = all([check_spot(ma, row + ind, col, player_num) for ind in range(slots_count)])
    is_right_up = all([check_spot(ma, row - ind, col + 1, player_num) for ind in range(slots_count)])
    is_left_up = all([check_spot(ma, row - ind, col - 1, player_num) for ind in range(slots_count)])
    is_right_down = all([check_spot(ma, row + ind, col + 1, player_num) for ind in range(slots_count)])
    is_left_down = all([check_spot(ma, row + ind, col - 1, player_num) for ind in range(slots_count)])

    if any([is_right, is_left, is_up, is_down, is_right_up, is_left_up, is_right_down, is_left_down]):
        return True
    return False


# create matrix
rows_count = 6
cols_count = 7
matrix = [[0 for col in range(cols_count)]for row in range(rows_count)]
print_matrix(matrix)

player_num = 1
while True:
    player_num = 2 if player_num % 2 == 0 else 1
    try:
        col_num = int(input(f"Player {player_num}, choose a column: ")) - 1
        validate_col_choice(col_num, cols_count - 1)
        row, col = place_player_choice(matrix, col_num, player_num)
        print_matrix(matrix)
        if is_winner(matrix, row, col, player_num):
            print(f"The winner is player {player_num}.")
            break

    except InvalidColError:
        print(f"This column number is not valid. Please select a number between {1} and {cols_count}")
        continue
    except ValueError:
        print(f"Please select a valid digit.")
        continue
    except FullColumnError:
        print("This column is already full, select a different one.")
        continue
    player_num += 1
