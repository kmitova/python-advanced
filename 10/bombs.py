from collections import deque

effects = deque([int(x) for x in input().split(', ')])
casings = [int(x) for x in input().split(', ')]
bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
enough = False
while effects and casings:
    if effects[0] + casings[-1] == 40 or effects[0] + casings[-1] == 60 or effects[0] + casings[-1] == 120:
        if effects[0] + casings[-1] == 40:
            bombs["Datura Bombs"] += 1
        elif effects[0] + casings[-1] == 60:
            bombs["Cherry Bombs"] += 1
        elif effects[0] + casings[-1] == 120:
            bombs["Smoke Decoy Bombs"] += 1
        effects.popleft()
        casings.pop()
    else:
        casings[-1] -= 5
    if bombs["Datura Bombs"] >= 3 and bombs["Cherry Bombs"] >= 3 and bombs["Smoke Decoy Bombs"] >= 3:
        enough = True
        break

if not enough:
    print("You don't have enough materials to fill the bomb pouch.")
if enough:
    print("Bene! You have successfully filled the bomb pouch!")

if effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in effects])}")
else:
    print("Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in casings])}")
else:
    print("Bomb Casings: empty")

sorted_bombs = sorted(bombs.items(), key=lambda kvp: kvp[0])
for key, value in sorted_bombs:
    print(f"{key}: {value}")
