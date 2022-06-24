from collections import deque

effects = deque([int(x) for x in input().split(', ')])
casings = [int(x) for x in input().split(', ')]
datura = 0
cherry = 0
smoke = 0
three_made = False
while casings and effects:
    if effects[0] + casings[-1] == 40:
        datura += 1
        effects.popleft()
        casings.pop()
    elif effects[0] + casings[-1] == 60:
        cherry += 1
        effects.popleft()
        casings.pop()
    elif effects[0] + casings[-1] == 120:
        smoke += 1
        effects.popleft()
        casings.pop()
    else:
        casings[-1] -= 5
    if cherry >= 3 and datura >= 3 and smoke >= 3:
        three_made = True
        break


if three_made:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in effects)}")
else:
    print("Bomb Effects: empty")
if casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in casings)}")
else:
    print("Bomb Casings: empty")


print(f"Cherry Bombs: {cherry}")

print(f"Datura Bombs: {datura}")

print(f"Smoke Decoy Bombs: {smoke}")
