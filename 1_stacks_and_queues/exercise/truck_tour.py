from collections import deque

circle = int(input())

queue = deque()

for i in range(circle):
    data = [int(x) for x in input().split()]
    queue.append(data)

for attempt in range(circle):
    tank = 0
    failed = False
    for fuel, distance in queue:
        tank += fuel
        if distance > tank:
            failed = True
            break
        else:
            tank -= distance

    if failed:
        queue.append(queue.popleft())
    else:
        print(attempt)
        break

