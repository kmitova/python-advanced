from collections import deque

# ramen: stack
# customers: queue

bowls = [int(el) for el in input().split(', ')]
customers = deque([int(el) for el in input().split(', ')])

while bowls and customers:
    bowl = bowls[-1]
    customer = customers[0]
    if bowls[-1] == customers[0]:
        bowls.pop()
        customers.popleft()
    elif bowls[-1] > customers[0]:
        bowls[-1] -= customers[0]
        customers.popleft()
    elif customers[0] > bowls[-1]:
        customers[0] -= bowls[-1]
        bowls.pop()

if customers and not bowls:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(el) for el in customers)}")

if not customers:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(el) for el in bowls)}")
