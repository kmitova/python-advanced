nums = [int(el) for el in input().split()]
target_num = int(input())
iterations = 0
unique = set()

for i in range(len(nums)):
    for j in range(len(nums)):
        if not i == j and i < j:
            if nums[i] + nums[j] == target_num:
                pair = (nums[i], nums[j])
                print(f"{nums[i]} + {nums[j]} = {target_num}")
                unique.add(pair)
            iterations += 1

print(f"Iterations done: {iterations}")
for el in unique:
    print(el)

