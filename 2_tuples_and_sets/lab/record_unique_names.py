# n = int(input())
# names = []
# for i in range(n):
#     name = input()
#     names.append(name)
#
# for name in set(names):
#     print(name)


# another solution
n = int(input())
names = set()
for i in range(n):
    name = input()
    names.add(name)

print("\n".join(names))
