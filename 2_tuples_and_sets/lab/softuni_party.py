n = int(input())
guests = set()
for i in range(n):
    code = input()
    guests.add(code)
came = set()
data = input()
while not data == "END":
    came.add(data)
    data = input()

result = guests.symmetric_difference(came)

print(len(result))

vips = []
regulars = []
for item in result:
    if item[0].isdigit():
        vips.append(item)
    else:
        regulars.append(item)
if vips:
    sorted_vips = sorted(vips)
    print("\n".join(sorted_vips))
if regulars:
    sorted_regulars = sorted(regulars)
    print("\n".join(sorted_regulars))
