import os

path = os.walk(".")
files_info = {}
for root, directories, files in path:
    for file in files:
        file_list = file.split('.')
        extension = '.' + file_list[1]
        if extension not in files_info:
            files_info[extension] = []
        files_info[extension].append(file)

with open('report.txt', 'w') as file:
    content = ''
    for key, values in files_info.items():
        content += f"{key}\n"
        for item in values:
            content += f"- - - {item}\n"
    file.write(content)

