n = int(input())
names = set()
for i in range(n):
    name = input()
    names.add(name)

print('\n'.join(names))
