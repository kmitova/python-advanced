def list_manipulator(nums, *args):
    if args:
        if args[0] == 'add' and args[1] == "beginning":
            to_add = list(args[2:])
            nums = to_add + nums
            return nums
        elif args[0] == 'add' and args[1] == "end":
            to_add = list(args[2:])
            nums = nums + to_add
            return nums
        elif args[0] == 'remove' and args[1] == "beginning":
            if len(args) > 2:
                for i in range(args[2]):
                    nums.pop(0)
            else:
                nums.pop(0)
            return nums
        elif args[0] == 'remove' and args[1] == "end":
            if len(args) > 2:
                for i in range(args[2]):
                    nums.pop()
            else:
                nums.pop()
            return nums


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
