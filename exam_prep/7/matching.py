from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches = 0
while males and females:
    if males[-1] % 25 == 0 and males[-1] != 0:
        males.pop()
        males.pop()
        continue
    if females[0] % 25 == 0 and females[0] != 0:
        females.popleft()
        females.popleft()
        continue
    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] <= 0:
        females.popleft()
        continue

    if males[-1] == females[0]:
        matches += 1
        males.pop()
        females.popleft()
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")
if males:
    males = reversed(males)
    print(f"Males left: {', '.join([str(x) for x in males])}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")


