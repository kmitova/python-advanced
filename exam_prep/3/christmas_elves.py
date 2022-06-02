from collections import deque

energy = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]
total_energy = 0
toys = 0
no_energy = False
no_materials = False
times = 0
while energy and materials:
    if energy[0] < 5:
        energy.popleft()
    else:
        times += 1
        if times % 3 == 0:
            if energy[0] >= materials[-1]*2:
                toys += 2
                total_energy += materials[-1]*2
                energy[0] -= materials[-1]*2
                new_energy = energy[0] + 1
                energy.popleft()
                energy.append(new_energy)
                materials.pop()
            else:
                energy[0] *= 2
                new_energy = energy[0]
                energy.popleft()
                energy.append(new_energy)
                continue
        else:
            if energy[0] >= materials[-1]:
                toys += 1
                energy[0] -= materials[-1]
                total_energy += materials[-1]
                new_energy = energy[0] + 1
                energy.popleft()
                energy.append(new_energy)
                materials.pop()
            else:
                energy[0] *= 2
                new_energy = energy[0]
                energy.popleft()
                energy.append(new_energy)
                continue
        if times % 5 == 0:
            if times % 3 == 0:
                toys -= 2
            else:
                toys -= 1
            energy[-1] -= 1


print(f"Toys: {toys}")
print(f"Energy: {total_energy}")

if energy:
    print(f"Elves left: {', '.join([str(x) for x in energy])}")
if materials:
    print(f"Boxes left: {', '.join([str(x) for x in materials])}")
