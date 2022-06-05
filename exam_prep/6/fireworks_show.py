from collections import deque

effects = deque([int(x) for x in input().split(', ')])
power = [int(x) for x in input().split(', ')]

palm = 0
willow = 0
crossette = 0

while effects and power:
    if effects[0] <= 0 or power[-1] <= 0:
        if effects[0] <= 0:
            effects.popleft()
        if power[-1] <= 0:
            power.pop()
        continue

    item_sum = effects[0] + power[-1]
    if item_sum % 3 == 0 and not item_sum % 5 == 0:
        palm += 1
        effects.popleft()
        power.pop()
    elif item_sum % 5 == 0 and not item_sum % 3 == 0:
        willow += 1
        effects.popleft()
        power.pop()
    elif item_sum % 5 == 0 and item_sum % 3 == 0:
        crossette += 1
        effects.popleft()
        power.pop()
    else:
        current_effect = effects[0] - 1
        effects.popleft()
        if not current_effect <= 0:
            effects.append(current_effect)

    if palm >= 3 and willow >= 3 and crossette >= 3:
        break

if palm >= 3 and willow >= 3 and crossette >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in effects])}")
if power:
    print(f"Explosive Power left: {', '.join([str(x) for x in power])}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")
