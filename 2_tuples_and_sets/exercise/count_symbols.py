text = list(input())
info = {}

for el in text:
    if el not in info:
        info[el] = 1
    else:
        info[el] += 1

sorted_info = sorted(info.items(), key=lambda x: x[0])

for data in sorted_info:
    print(f"{data[0]}: {data[1]} time/s")
