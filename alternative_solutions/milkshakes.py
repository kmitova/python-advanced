from collections import deque

chocolate = [int(x) for x in input().split(', ')]
milk = deque([int(x) for x in input().split(', ')])
milkshakes_made = 0
enough_milkshakes = False
while milk and chocolate:
    if milk[0] <= 0 or chocolate[-1] <= 0:
        if milk[0] <= 0:
            milk.popleft()
        if chocolate[-1] <= 0:
            chocolate.pop()
    else:
        if milk[0] == chocolate[-1]:
            milkshakes_made += 1
            milk.popleft()
            chocolate.pop()
        else:
            milk_to_move = milk[0]
            milk.popleft()
            milk.append(milk_to_move)
            chocolate[-1] -= 5
    if milkshakes_made  >= 5:
        enough_milkshakes = True
        break

if enough_milkshakes:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join(str(x) for x in milk)}")
else:
    print("Milk: empty")
