from collections import deque

# cups: queue
# bottles: stack
#  fill all cups (queue)
cups = deque([int(y) for y in input().split()])
bottles = [int(x) for x in input().split()]
wasted_water = 0
current_left = 0
left_bottles = 0

while cups or bottles:
    if len(cups) == 0 or len(bottles) == 0:
        break
    cup = cups[0]
    bottle = bottles[-1]
    water_in_bottle = bottle
    cup -= bottle
    bottles.pop()
    if cup <= 0:
        cups.popleft()
        current_left += abs(cup)
    else:
        # cup -= bottles[-1]
        # bottles.pop()
        cups[0] = cup

# print(bottles)
# print(cups)
#
#
# print(current_left)

if bottles:
    bottles = [str(i) for i in bottles]
    print(f"Bottles: {' '.join(bottles)}")
elif cups:
    cups = [str(i) for i in cups]
    print(f"Cups: {' '.join(cups)}")
print(f"Wasted litters of water: {current_left}")









# while cups or bottles:
#     if len(cups) == 0 or len(bottles) == 0:
#         break
#     cup = cups[0]
#     bottle = bottles[-1]
#     initial_bottle = bottle
#     current_left = bottle - cup
#     # if current_left > 0:
#
#     bottles.pop()
#     if cup - bottle <= 0:
#         cups.popleft()
#     wasted_water += current_left
#     current_left = 0
#     # bottle -= cup
#     # cup = cup - initial_bottle
#     #
#     # print(bottle)
#     # if cup <= 0:
#     #     cups.popleft()
#     # if bottle > 0 and cups:
#     #     current_left += bottle
#     #     bottles.pop()
#     #     left_bottles += 1
#     # else:
#     #     bottles.pop()
#
# print(wasted_water)
#
# if len(bottles) > 0:
#     print(f"Bottles: {bottles}")
# if len(cups) > 0:
#     print(cups)
