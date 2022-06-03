size = 6
matrix = []
points = 0
for row in range(size):
    data = input().split()
    matrix.append(data)

for throw in range(3):
    info = input()
    info = info.replace("(", "")
    info = info.replace(")","")
    coords = [int(x) for x in info.split(", ")]
    row = coords[0]
    col = coords[1]
    # two runtime errors with continue
    # if row not in range(0, size) and col not in range(0, size):
    #     continue
    if row in range(0, size) and col in range(0, size):
        if matrix[row][col] == 'B':
            matrix[row][col] = 'x'
            for i in range(size):
                if matrix[i][col] != "x":
                    points += int(matrix[i][col])

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
else:
    if points >= 300:
        print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
    elif 200 <= points <= 299:
        print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
    elif 100 <= points <= 199:
        print(f"Good job! You scored {points} points, and you've won Football.")
