from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
enough_nectar = False
honey_made = 0
while bees and nectar:
    if nectar[-1] >= bees[0]:
        enough_nectar = True
    else:
        nectar.pop()
    if enough_nectar:
        current_honey = 0
        if symbols[0] == '+':
            current_honey = abs(bees[0] + nectar[-1])
        elif symbols[0] == '-':
            current_honey = abs(bees[0] - nectar[-1])
        elif symbols[0] == '*':
            current_honey = abs(bees[0] * nectar[-1])
        elif symbols[0] == '/' and nectar[-1] != 0:
            current_honey = abs(bees[0] / nectar[-1])
        honey_made += current_honey
        bees.popleft()
        nectar.pop()
        symbols.popleft()
        enough_nectar = False

print(f"Total honey made: {honey_made}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
