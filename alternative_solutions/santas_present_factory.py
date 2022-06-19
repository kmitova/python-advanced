from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])
presents = {"Doll": 0,
            "Wooden train": 0,
            "Teddy bear": 0,
            "Bicycle": 0}

doll_and_train = False
bear_and_bicycle = False

while magic and materials:
        if magic[0] * materials[-1] == 150:
            presents["Doll"] += 1
            magic.popleft()
            materials.pop()
        elif magic[0] * materials[-1] == 250:
            presents["Wooden rain"] += 1
            magic.popleft()
            materials.pop()
        elif magic[0] * materials[-1] == 300:
            presents["Teddy bear"] += 1
            magic.popleft()
            materials.pop()
        elif magic[0] * materials[-1] == 400:
            presents["Bicycle"] += 1
            magic.popleft()
            materials.pop()

        elif magic[0] * materials[-1] < 0:
            sum_values = magic[0] + materials[-1]
            magic.popleft()
            materials.pop()
            materials.append(sum_values)
        elif magic[0] * materials[-1] > 0:
            magic.popleft()
            materials[-1] += 15
        elif magic[0] == 0 or materials[-1] == 0:
            if magic[0] == 0:
                magic.popleft()
            if materials[-1] == 0:
                materials.pop()
        if presents["Doll"] >= 1 and presents['Wooden train'] >= 1:
            doll_and_train = True
        if presents["Teddy bear"] >= 1 and presents['Bicycle'] >= 1:
            bear_and_bicycle = True

if doll_and_train or bear_and_bicycle:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

sorted_presents = sorted(presents.items(), key=lambda kvp: kvp[0])

for key, value in sorted_presents:
    if value > 0:
        print(f"{key}: {value}")
