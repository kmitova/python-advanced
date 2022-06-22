from collections import deque

palms = 0
willows = 0
crossettes = 0
effects = deque([int(x) for x in input().split(', ')])
powers = [int(x) for x in input().split(', ')]

while effects and powers:
    if effects[0] <= 0 or powers[-1] <= 0:
        if effects[0] <= 0:
            effects.popleft()
        if powers[-1] <= 0:
            powers.pop()
    else:
        result = effects[0] + powers[-1]
        if result % 3 == 0 and result % 5 != 0:
            palms += 1
            powers.pop()
            effects.popleft()
        elif result % 5 == 0 and result % 3 != 0:
            willows += 1
            powers.pop()
            effects.popleft()
        elif result % 5 == 0 and result % 3 == 0:
            crossettes += 1
            powers.pop()
            effects.popleft()
        else:
            effects[0] -= 1
            add = effects[0]
            effects.popleft()
            effects.append(add)
    if willows >= 3 and crossettes >= 3 and palms >= 3:
        break

if willows >= 3 and crossettes >= 3 and palms >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in effects)}")
if powers:
    print(f"Explosive Power left: {', '.join(str(x) for x in powers)}")

print(f"Palm Fireworks: {palms}")
print(f"Willow Fireworks: {willows}")
print(f"Crossette Fireworks: {crossettes}")

