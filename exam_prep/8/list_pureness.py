from collections import deque
from sys import maxsize


def best_list_pureness(*args):
    numbers = deque(args[0])
    n = int(args[1])
    best_pureness = -maxsize
    rotations = 0
    best_rotations = 0
    for i in range(n+1):
        current_pureness = 0
        if i == 0:
            for ind in range(len(numbers)):
                current_pureness += ind * numbers[ind]
        else:
            numbers.rotate()
            for ind in range(len(numbers)):
                current_pureness += ind * numbers[ind]
        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rotations = rotations
        rotations += 1
    return f"Best pureness {best_pureness} after {best_rotations} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
