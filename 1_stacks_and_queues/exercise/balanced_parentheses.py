sequence = input()

opening = []
balanced = True
for el in sequence:
    if el in "{[(":
        opening.append(el)
    elif not opening:
        balanced = False
        break
    else:
        last_opening = opening.pop()
        if f"{last_opening}{el}" not in "(){}[]":
            balanced = False
            break

if balanced:
    print("YES")
else:
    print("NO")
