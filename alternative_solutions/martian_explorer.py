def move_right(row, col, size):
    if col + 1 < size:
        return row, col + 1
    else:
        return row, 0


def move_down(row, col, size):
    if row + 1 < size:
        return row + 1, col
    else:
        return 0, col


def move_left(row, col, size):
    if col - 1 >= 0:
        return row, col - 1
    else:
        return row, size - 1


def move_up(row, col, size):
    if row - 1 >= 0:
        return row-1, col
    else:
        return size - 1, col


size = 6
matrix = []
rover_row = 0
rover_col = 0
broken_at_rock = False
water = 0
metal = 0
concrete = 0

for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        element = data[col]
        if element == "E":
            rover_row = row
            rover_col = col

commands = input().split(', ')

for direction in commands:
    if direction == 'right':
        rover_row, rover_col = move_right(rover_row, rover_col, size)
    elif direction == 'down':
        rover_row, rover_col = move_down(rover_row, rover_col, size)
    elif direction == 'left':
        rover_row, rover_col = move_left(rover_row, rover_col, size)
    elif direction == 'up':
        rover_row, rover_col = move_up(rover_row, rover_col, size)
    if matrix[rover_row][rover_col] == 'R':
        broken_at_rock = True
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break
    if matrix[rover_row][rover_col] == 'W':
        water += 1
        print(f"Water deposit found at ({rover_row}, {rover_col})")
    if matrix[rover_row][rover_col] == 'C':
        concrete += 1
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")
    if matrix[rover_row][rover_col] == 'M':
        metal += 1
        print(f"Metal deposit found at ({rover_row}, {rover_col})")
    matrix[rover_row][rover_col] = '-'

if water >= 1 and metal >= 1 and concrete >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

