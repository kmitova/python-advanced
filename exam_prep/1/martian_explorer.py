def move_up(row, col):
    return row-1, col


def move_down(row, col):
    return row+1, col


def move_right(row, col):
    return row, col+1


def move_left(row, col):
    return row, col-1


size = 6
matrix = []

rover_row = 0
rover_col = 0
water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

must_stop = False


for row in range(size):
    data = input().split()
    matrix.append(data)
    for col in range(size):
        element = data[col]
        if element == "E":
            rover_row = row
            rover_col = col

commands = input().split(', ')

for command in commands:
    if command == 'down':
        matrix[rover_row][rover_col] = '-'
        if 0 <= rover_row+1 < size:
            if matrix[rover_row + 1][rover_col] == "R":
                must_stop = True
            if matrix[rover_row + 1][rover_col] == "W":
                water_deposit += 1
                print(f"Water deposit found at ({rover_row+1}, {rover_col})")
            if matrix[rover_row + 1][rover_col] == "M":
                metal_deposit += 1
                print(f"Metal deposit found at ({rover_row + 1}, {rover_col})")
            if matrix[rover_row + 1][rover_col] == "C":
                concrete_deposit += 1
                print(f"Concrete deposit found at ({rover_row + 1}, {rover_col})")
            matrix[rover_row+1][rover_col] = '-'
            rover_row = rover_row + 1

        elif rover_row + 1 > size - 1:
            rover_row = 0
            if matrix[0][rover_col] == "R":
                must_stop = True
            if matrix[0][rover_col] == "W":
                water_deposit += 1
                print(f"Water deposit found at ({rover_row}, {rover_col})")
            if matrix[0][rover_col] == "M":
                metal_deposit += 1
                print(f"Metal deposit found at ({rover_row}, {rover_col})")
            if matrix[0][rover_col] == "C":
                concrete_deposit += 1
                print(f"Concrete deposit found at ({rover_row}, {rover_col})")

    if command == "right":
        matrix[rover_row][rover_col] = '-'
        if 0 <= rover_col + 1 < size:
            if matrix[rover_row][rover_col+1] == "R":
                must_stop = True
            if matrix[rover_row][rover_col+1] == "W":
                water_deposit += 1
                print(f"Water deposit found at ({rover_row}, {rover_col+1})")
            if matrix[rover_row][rover_col+1] == "M":
                metal_deposit += 1
                print(f"Metal deposit found at ({rover_row}, {rover_col+1})")
            if matrix[rover_row][rover_col+1] == "C":
                concrete_deposit += 1
                print(f"Concrete deposit found at ({rover_row}, {rover_col+1})")
            matrix[rover_row][rover_col+1] = '-'
            rover_col = rover_col + 1

        elif rover_col + 1 > size - 1:
            rover_col = 0
            if matrix[rover_row][0] == "R":
                must_stop = True
            if matrix[rover_row][0] == "W":
                water_deposit += 1
                print(f"Water deposit found at ({rover_row}, {rover_col})")
            if matrix[rover_row][0] == "M":
                metal_deposit += 1
                print(f"Metal deposit found at ({rover_row}, {rover_col})")
            if matrix[rover_row][0] == "C":
                concrete_deposit += 1
                print(f"Concrete deposit found at ({rover_row}, {rover_col})")

    if command == "left":
        matrix[rover_row][rover_col] = '-'
        if 0 <= rover_col - 1 < size:
            if matrix[rover_row][rover_col-1] == "R":
                must_stop = True
            if matrix[rover_row][rover_col-1] == "W":
                water_deposit += 1
                print(f"Water deposit found at ({rover_row}, {rover_col-1})")
            if matrix[rover_row][rover_col-1] == "M":
                metal_deposit += 1
                print(f"Metal deposit found at ({rover_row}, {rover_col-1})")
            if matrix[rover_row][rover_col-1] == "C":
                concrete_deposit += 1
                print(f"Concrete deposit found at ({rover_row}, {rover_col-1})")
            matrix[rover_row][rover_col-1] = '-'
            rover_col = rover_col - 1

        elif rover_col - 1 < 0:
            rover_col = size - 1
            if matrix[rover_row][-1] == "R":
                must_stop = True
            if matrix[rover_row][-1] == "W":
                water_deposit += 1
                print(f"Water deposit found at ({rover_row}, {rover_col})")
            if matrix[rover_row][-1] == "M":
                metal_deposit += 1
                print(f"Metal deposit found at ({rover_row}, {rover_col})")
            if matrix[rover_row][-1] == "C":
                concrete_deposit += 1
                print(f"Concrete deposit found at ({rover_row}, {rover_col})")
    if command == "up":
        matrix[rover_row][rover_col] = '-'
        if 0 <= rover_row - 1 < size:
            if matrix[rover_row - 1][rover_col] == "R":
                must_stop = True
            if matrix[rover_row - 1][rover_col] == "W":
                water_deposit += 1
                print(f"Water deposit found at ({rover_row - 1}, {rover_col})")
            if matrix[rover_row - 1][rover_col] == "M":
                metal_deposit += 1
                print(f"Metal deposit found at ({rover_row - 1}, {rover_col})")
            if matrix[rover_row - 1][rover_col] == "C":
                concrete_deposit += 1
                print(f"Concrete deposit found at ({rover_row - 1}, {rover_col})")
            matrix[rover_row - 1][rover_col] = '-'
            rover_row = rover_row - 1

        elif rover_row - 1 < 0:
            rover_row = size - 1
            if matrix[-1][rover_col] == "R":
                must_stop = True
            if matrix[-1][rover_col] == "W":
                water_deposit += 1
                print(f"Water deposit found at ({rover_row}, {rover_col})")
            if matrix[-1][rover_col] == "M":
                metal_deposit += 1
                print(f"Metal deposit found at ({rover_row}, {rover_col})")
            if matrix[-1][rover_col] == "C":
                concrete_deposit += 1
                print(f"Concrete deposit found at ({rover_row}, {rover_col})")

    if must_stop:
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

if water_deposit > 0 and metal_deposit > 0 and concrete_deposit > 0:
    print(f"Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
