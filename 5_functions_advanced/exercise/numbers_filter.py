def even_odd_filter(**kwargs):
    nums = {}
    for key, value in kwargs.items():
        if key == 'odd':
            nums['odd'] = []
            for el in value:
                if not el % 2 == 0:
                    nums['odd'].append(el)
        elif key == 'even':
            nums['even'] = []
            for el in value:
                if el % 2 == 0:
                    nums['even'].append(el)
    sorted_nums = sorted(nums.items(), key=lambda kvp: -len(kvp[1]))
    return dict(sorted_nums)


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5, 15],
))
