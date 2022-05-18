from collections import deque

# magic values is deque queue
# boxes is stack

boxes = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])

success = False
presents = {'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}
while boxes and magic_values:
    box = boxes[-1]
    value = magic_values[0]
    if box*value == 150:
        presents['Doll'] += 1
        boxes.pop()
        magic_values.popleft()
    elif box * value == 250:
        presents['Wooden train'] += 1
        boxes.pop()
        magic_values.popleft()
    elif box * value == 300:
        presents['Teddy bear'] += 1
        boxes.pop()
        magic_values.popleft()
    elif box * value == 400:
        presents['Bicycle'] += 1
        boxes.pop()
        magic_values.popleft()
    elif box * value < 0:
        result = box + value
        boxes.pop()
        magic_values.popleft()
        boxes.append(result)
    elif box * value > 0:
        magic_values.popleft()
        boxes[-1] = box + 15
    elif box == 0 or value == 0:
        if box == 0:
            boxes.pop()
        if value == 0:
            magic_values.popleft()

    if presents['Doll'] >= 1 and presents['Wooden train'] >= 1:
        success = True

    if presents['Teddy bear'] >= 1 and presents['Bicycle'] >= 1:
        success = True


if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes:
    print(f"Materials left: {', '.join((str(i) for i in boxes[::-1]))}")
if magic_values:
    print(f"Magic left: {', '.join((str(i) for i in magic_values))}")


sorted_presents = sorted(presents.items(), key=lambda x: x[0])
for data in sorted_presents:
    if int(data[1]) > 0:
        print(f"{data[0]}: {data[1]}")
