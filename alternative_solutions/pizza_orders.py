from collections import deque

orders = deque([int(x) for x in input().split(', ')])
employees = [int(x) for x in input().split(', ')]
pizzas = 0

while orders and employees:
    if orders[0] > 10:
        orders.popleft()
    elif orders[0] <= 0:
        orders.popleft()
    else:
        if orders[0] <= employees[-1]:
            pizzas += orders[0]
            orders.popleft()
            employees.pop()
        else:
            pizzas += employees[-1]
            orders[0] -= employees[-1]
            employees.pop()

if not orders:
    print('All orders are successfully completed!')
    print(f"Total pizzas made: {pizzas}")
if employees:
    print(f"Employees: {', '.join(str(x) for x in employees)}")

if orders and not employees:
    print('Not all orders are completed.')
    print(f"Orders left: {', '.join(str(x) for x in orders)}")
