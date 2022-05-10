from collections import deque

food = int(input())

sequence = input().split()
sequence_queue = deque([int(i) for i in sequence])

print(max(sequence_queue))
food_out = False

while sequence_queue:
    order = sequence_queue[0]
    if order <= food:
        sequence_queue.popleft()
        food -= order
    else:
        food_out = True
        break

if len(sequence_queue) == 0:
    print("Orders complete")
else:
    sequence_queue = [str(i) for i in sequence_queue]
    print(f"Orders left: {' '.join(sequence_queue)}")



