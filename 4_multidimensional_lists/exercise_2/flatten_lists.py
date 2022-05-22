string = input().split("|")

result = []

while string:
    sublist = string.pop().split()
    for el in sublist:
        result.append(el)


print(*result, sep=" ")
