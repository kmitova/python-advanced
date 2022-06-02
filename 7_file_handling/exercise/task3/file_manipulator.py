import os

data = input()
while not data == "End":
    line = data.split('-')
    command = line[0]
    file_name = line[1]
    if command == 'Create':
        open(file_name, 'w').close()
    elif command == "Add":
        content = line[2]
        with open(file_name, 'a') as file:
            file.write(content + '\n')
    elif command == 'Replace':
        if os.path.exists(file_name):
            old_string = line[2]
            new_string = line[3]
            with open(file_name, 'r+') as file:
                new_text = file.read().replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(new_text)
        else:
            print("An error occurred")
    elif command == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")
    data = input()
