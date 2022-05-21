rows, cols = [int(el) for el in input().split()]

matrix = []
ind = 0
word = input()

for row in range(rows):
    row_elements = []
    for col in range(cols):
        row_elements.append(word[ind % len(word)])
        ind += 1
    if row % 2 == 0:
        print(*row_elements, sep='')
    else:
        print(*reversed(row_elements), sep='')



