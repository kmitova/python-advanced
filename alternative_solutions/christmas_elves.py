from collections import deque

elves = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]
total_energy = 0
toys = 0
times = 0
while elves and materials:
    if elves[0] < 5:
        elves.popleft()
    else:
        box = materials.pop()
        energy = elves.popleft()
        times += 1
        toys_to_make = 1
        energy_spent = box
        energy_increase = 1
        if times % 3 == 0:
            toys_to_make = 2
            energy_spent *= 2
        if times % 5 == 0:
            toys_to_make = 0
            energy_increase = 0
        if energy_spent <= energy:
            toys += toys_to_make
            total_energy += energy_spent
            elves.append(energy - energy_spent + energy_increase)
        else:
            materials.append(box)
            elves.append(energy * 2)

print(f'Toys: {toys}')
print(f'Energy: {total_energy}')
if elves:
    elves_str = ', '.join(str(x) for x in elves)
    print(f"Elves left: {elves_str}")
if materials:
    boxes_str = ', '.join(str(x) for x in materials)
    print(f"Boxes left: {boxes_str}")



