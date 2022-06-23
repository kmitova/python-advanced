from collections import deque


def best_list_pureness(nums, k):
    max_pureness = -9999999
    rotations = 0
    best_rotations = 0
    nums = deque(nums)
    for i in range(k+1):
        current_pureness = 0
        if i == 0:
            for ind in range(len(nums)):
                current_pureness += ind * nums[ind]
        else:

            nums.rotate()
            for ind in range(len(nums)):
                current_pureness += ind * nums[ind]
        if current_pureness > max_pureness:
            max_pureness = current_pureness
            best_rotations = rotations
        rotations += 1
    return f"Best pureness {max_pureness} after {best_rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
