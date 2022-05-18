first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())
n = int(input())

for i in range(n):
    command = input().split()
    if len(command) > 2:
        action = command[0]
        which_sequence = command[1]
        if action == "Add":
            if which_sequence == "First":
                [first_sequence.add(int(x)) for x in command[2:]]
            elif which_sequence == "Second":
                [second_sequence.add(int(x)) for x in command[2:]]
        elif action == "Remove":
            if which_sequence == "First":
                first_sequence = first_sequence.difference([int(x) for x in command[2:]])
            elif which_sequence == "Second":
                second_sequence = second_sequence.difference([int(x) for x in command[2:]])

    else:
        print(first_sequence.issubset(second_sequence) or (second_sequence.issubset(first_sequence)))


print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")

