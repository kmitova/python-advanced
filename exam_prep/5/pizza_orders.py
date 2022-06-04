from collections import deque

pizzas = deque([int(x) for x in input().split(', ')])
employees = [int(x) for x in input().split(', ')]
made = 0
# take first order and last employee
while pizzas and employees:
    if pizzas[0] > 10:
        pizzas.popleft()
        continue
    if pizzas[0] <= 0:
        pizzas.popleft()
        continue
    if pizzas[0] <= employees[-1]:
        made += pizzas[0]
        pizzas.popleft()
        employees.pop()
    else:
        made += employees[-1]
        pizzas[0] -= employees[-1]
        employees.pop()

if not pizzas:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {made}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")

if not employees:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizzas)}")
