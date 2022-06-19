from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]

wasted = 0

while cups and bottles:
    cups[0] -= bottles[-1]
    bottles.pop()
    if cups[0] <= 0:
        wasted += abs(cups[0])
        cups.popleft()

if cups:
    print(f"Cups: {' '.join(str(x) for x in cups)}")
if bottles:
    print(f"Bottles: {' '.join(str(x) for x in bottles)}")

print(f"Wasted litters of water: {wasted}")
