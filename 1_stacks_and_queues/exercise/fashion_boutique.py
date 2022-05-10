sequence = input().split()

sequence_stack = [int(i) for i in sequence]


rack_capacity = int(input())
total_racks = 1

total_values = 0
current_sum = 0
while sequence_stack:
    current = sequence_stack.pop()
    if current_sum + current <= rack_capacity:
        current_sum += current
    elif current_sum + current > rack_capacity:
        total_racks += 1
        sequence_stack.append(current)
        current_sum = 0

print(total_racks)

