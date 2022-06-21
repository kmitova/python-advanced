from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])
presents = {'Gemstone': 0, 'Porcelain Sculpture': 0, 'Gold': 0, 'Diamond Jewellery': 0}
gemstone_and_sculpture = False
gold_and_jewellery = False
count = 0
while magic and materials:
    result = magic[0] + materials[-1]

    if 100 <= result <= 499:
        if result <= 199:
            presents["Gemstone"] += 1
        elif result <= 299:
            presents['Porcelain Sculpture'] += 1
        elif result <= 399:
            presents['Gold'] += 1
        elif result <= 499:
            presents['Diamond Jewellery'] += 1
        magic.popleft()
        materials.pop()
    elif result < 100:
        if result % 2 == 0:
            materials[-1] *= 2
            magic[0] *= 3
            count = 1
        else:
            materials[-1] *= 2
            magic[0] *= 2
            count = 1
        if materials[-1] + magic[0] < 100:
            materials.pop()
            magic.popleft()
    elif result > 499:
        materials[-1] /= 2
        magic[0] /= 2
        if materials[-1] + magic[0] > 499:
            materials.pop()
            magic.popleft()
    else:
        materials.pop()
        magic.popleft()

    if presents["Gemstone"] >= 1 and presents['Porcelain Sculpture'] >= 1:
        gemstone_and_sculpture = True
    if presents['Gold'] >= 1 and presents['Diamond Jewellery'] >= 1:
        gold_and_jewellery = True

if gemstone_and_sculpture or gold_and_jewellery:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")

if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

sorted_presents = sorted(presents.items())
for key, value in sorted_presents:
    if value > 0:
        print(f"{key}: {value}")
