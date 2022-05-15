n_str, m_str = input().split()

n = int(n_str)
m = int(m_str)
set_n = set()
set_m = set()

for i in range(n):
    data = int(input())
    set_n.add(data)

for i in range(m):
    data = int(input())
    set_m.add(data)

result = set_n.intersection(set_m)

print("\n".join(str(el) for el in result))
