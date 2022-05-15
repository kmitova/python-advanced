n = int(input())

odd = set()
even = set()
current = 0
for i in range(n):
    name = input()
    ascii_sum = 0
    current += 1
    for el in name:
        ascii_sum += ord(el)
    ascii_sum_div = int(ascii_sum / current)
    if not ascii_sum_div % 2 == 0:
        odd.add(ascii_sum_div)
    else:
        even.add(ascii_sum_div)

if sum(odd) == sum(even):
    union_sets = odd.union(even)
    print(", ".join(str(el) for el in union_sets))

elif sum(odd) < sum(even):
    sym_diff = odd.symmetric_difference(even)
    print(", ".join(str(el) for el in sym_diff))

else:
    diff = odd.difference(even)
    print(", ".join(str(el) for el in diff))
