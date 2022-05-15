n = int(input())
unique = set()
for i in range(n):
    data = input().split()
    for el in data:
        unique.add(el)

print("\n".join(unique))
