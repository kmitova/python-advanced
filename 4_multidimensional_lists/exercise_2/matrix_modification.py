n = int(input())

matrix = []

for i in range(n):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

command = input()
while not command == "END":
    data = command.split()
    action = data[0]
    row = int(data[1])
    col = int(data[2])
    value = int(data[3])
    if row in range(n) and col in range(n):
        if action == "Add":
            matrix[row][col] += value
        elif action == 'Subtract':
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    command = input()

for row in matrix:
    print(*row, sep=' ')
