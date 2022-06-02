try:
    # 'with... as...:' opens and then automatically
    # closes the file to save memory
    with open('numbers.txt') as file:
        print(sum([int(line) for line in file.readlines()]))
except FileNotFoundError:
    print("File not found.")
