size = 6
matrix = []
points = 0

for row in range(size):
    data = input().split()
    matrix.append(data)

for throw in range(3):
    data = input()
    data = data.replace('(', '')
    data = data.replace(')', '')
    row_str, col_str = data.split(', ')
    row = int(row_str)
    col = int(col_str)
    if row in range(size) and col in range(size):
        if matrix[row][col] == 'B':
            matrix[row][col] = 0
            for i in range(size):
                points += int(matrix[i][col])

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
elif points < 200:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif points < 300:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif points >= 300:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")

