def fix_calendar(nums):
    for i in range(len(nums)):
        for k in range(len(nums)):
            if nums[i] < nums[k]:
                nums[i], nums[k] = nums[k], nums[i]

    return nums


numbers = [3, 2, 1]
fixed = fix_calendar(numbers)
print(fixed)
