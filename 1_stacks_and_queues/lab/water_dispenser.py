from collections import deque
# append, popleft
water = int(input())
line = deque()

command = input()
while not command == "Start":
    line.append(command)
    command = input()

data = input()
while not data == "End":
    data = data.split()
    if len(data) == 1:
        liters = int(data[0])
        name = line.popleft()
        if water >= liters:
            water -= liters
            print(f"{name} got water")
        else:
            print(f"{name} must wait")
    else:
        liters = int(data[1])
        water += liters
    data = input()

print(f"{water} liters left")
