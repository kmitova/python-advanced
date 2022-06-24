def numbers_searching(*args):
    missing_num = 0
    duplicates = []
    duplicates = list(set([x for x in args if x in duplicates or duplicates.append(x)]))
    duplicates = sorted(list(duplicates))
    args = sorted(args)
    for ind in range(len(args)-1):
        if args[ind] < args[ind+1]-1:
            if args[ind] + 1 < max(args):
                missing_num = args[ind] + 1
                break

    result = [missing_num, (duplicates)]
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
