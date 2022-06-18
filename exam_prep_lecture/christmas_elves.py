from collections import deque

energies = deque([int(x) for x in input().split()])
boxes = [int(x) for x in input().split()]

turns = 0
total_energy = 0
toys = 0

while boxes and energies:

    while energies and energies[0] < 5:
        energies.popleft()
    if not energies:
        break
    box = boxes.pop()
    energy = energies.popleft()
    turns += 1
    toys_to_make = 1
    energy_spent = box
    energy_increase = 1
    if turns % 3 == 0:
        toys_to_make = 2
        energy_spent *= 2

    if turns % 5 == 0:
        toys_to_make = 0
        energy_increase = 0

    if energy_spent <= energy:
        toys += toys_to_make
        total_energy += energy_spent
        energies.append(energy - energy_spent + energy_increase)
    else:
        boxes.append(box)
        energies.append(energy * 2)

print(f'Toys: {toys}')
print(f'Energy: {total_energy}')
if energies:
    elves_str = ', '.join(str(x) for x in energies)
    print(f"Elves left: {elves_str}")
if boxes:
    boxes_str = ', '.join(str(x) for x in boxes)
    print(f"Boxes left: {boxes_str}")
