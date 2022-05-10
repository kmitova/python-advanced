from collections import deque

green_duration = int(input())
window = int(input())
total_time = green_duration + window
cars = deque()
command = input()
passed_count = 0
crash = False
while not command == 'END':
    if not command == "green":
        car = command
        cars.append(car)
    elif command == "green":
        total_time = green_duration + window
        while cars:
            car = cars[0]
            if total_time > window:
                if len(car) <= total_time:
                    passed_count += 1
                    cars.popleft()
                    total_time -= len(car)
                else:
                    crash = True
                    print("A crash happened!")
                    print(f"{car} was hit at {car[total_time]}.")
                    break
            else:
                break
    if crash:
        break

    command = input()

if not crash:
    print("Everyone is safe.")
    print(f"{passed_count} total cars passed the crossroads.")
