from collections import deque
items = {'Gemstone': 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}
materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])
gem_and_sculpture = False
gold_and_diamond = False
while magic and materials:
    item_sum = materials[-1] + magic[0]
    if 100 <= item_sum <= 499:
        if 100 <= item_sum <= 199:
            items["Gemstone"] += 1
        elif 200 <= item_sum <= 299:
            items["Porcelain Sculpture"] += 1
        elif 300 <= item_sum <= 399:
            items["Gold"] += 1
        elif 400 <= item_sum <= 499:
            items["Diamond Jewellery"] += 1
        materials.pop()
        magic.popleft()
    else:
        if item_sum < 100:
            if item_sum % 2 == 0:
                materials[-1] *= 2
                magic[0] *= 3
            else:
                materials[-1] *= 2
                magic[0] *= 2
            if 100 <= materials[-1] + magic[0] <= 499:
                continue
        elif item_sum > 499:
            materials[-1] /= 2
            magic[0] /= 2
            if materials[-1] + magic[0] <= 499:
                continue
        materials.pop()
        magic.popleft()

if items["Gemstone"] > 0 and items["Porcelain Sculpture"] > 0:
    gem_and_sculpture = True

if items["Diamond Jewellery"] > 0 and items["Gold"] > 0:
    gold_and_diamond = True


if gem_and_sculpture or gold_and_diamond:
    print("The wedding presents are made!")
if not gem_and_sculpture and not gold_and_diamond:
    print("Aladdin does not have enough wedding presents.")

if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
sorted_items = sorted(items.items(), key=lambda kvp: kvp[0])
for key, value in sorted_items:
    if value > 0:
        print(f"{key}: {value}")
