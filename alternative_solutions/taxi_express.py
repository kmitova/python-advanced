from collections import deque

customers = deque([int(x) for x in input().split(', ')])
taxis = [int(x) for x in input().split(', ')]
time = 0

while taxis and customers:
    if taxis[-1] >= customers[0]:
        time += customers[0]
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {time} minutes")
if not taxis and customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
