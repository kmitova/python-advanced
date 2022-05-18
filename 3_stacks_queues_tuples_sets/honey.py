from collections import deque

# bees is deque queue
# nectar is stack

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
total_honey = 0

while bees and nectar:
    bee = bees[0]
    current_nectar = nectar[-1]
    if current_nectar >= bee:
        honey = 0
        symbol = symbols[0]
        if symbol == '+':
            honey = bee + current_nectar
        elif symbol == "-":
            honey = bee - current_nectar
        elif symbol == "*":
            honey = bee * current_nectar
        elif symbol == "/" and current_nectar != 0:

            honey = bee / current_nectar
        honey = abs(honey)
        # print(honey)
        total_honey += honey
        bees.popleft()
        nectar.pop()
        symbols.popleft()
    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join((str(i) for i in bees))}")
if nectar:
    print(f"Nectar left: {', '.join((str(i) for i in nectar))}")
