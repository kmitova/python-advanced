from collections import deque
males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches = 0
while males and females:
    if males[-1] <= 0 or females[0] <= 0:
        if males[-1] <= 0:
            males.pop()
        if females[0] <= 0:
            females.popleft()
    elif males[-1] % 25 == 0 or females[0] % 25 == 0:
        if males[-1] % 25 == 0:
            males.pop()
            males.pop()
        if females[0] % 25 == 0:
            females.popleft()
            females.popleft()
    else:
        if females[0] == males[-1]:
            matches += 1
            females.popleft()
            males.pop()
        else:
            females.popleft()
            males[-1] -= 2

print(f"Matches: {matches}")
if males:
    males = males[::-1]
    print(f"Males left: {', '.join((str(x) for x in males))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join((str(x) for x in females))}")
else:
    print("Females left: none")
