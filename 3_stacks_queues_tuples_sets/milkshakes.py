from collections import deque

# milk is deque queue
# choco is stack

choco = [int(x) for x in input().split(", ")]
milk = deque([int(x) for x in input().split(", ")])

five_milkshakes = False
counter = 0
while choco and milk:
    current_choco = choco.pop()
    current_milk = milk.popleft()
    if current_choco <= 0 and current_milk <= 0:
        continue

    if current_choco <= 0:
        milk.appendleft(current_milk)
        continue

    if current_milk <= 0:
        choco.append(current_choco)
        continue

    if current_milk == current_choco:
        counter += 1
    else:
        choco.append(current_choco - 5)
        milk.append(current_milk)
    if counter == 5:
        five_milkshakes = True
        break

if five_milkshakes:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if choco:
    print(f"Chocolate: {', '.join((str(i) for i in choco))}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join((str(i) for i in milk))}")
else:
    print("Milk: empty")
