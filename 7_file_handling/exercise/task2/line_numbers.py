import re

with open('text.txt') as file, open('output.txt', 'w') as output_file:
    for i, line in enumerate(file):
        pattern = fr'[A-Za-z]'
        str_line = line.strip()
        letters = len(re.findall(pattern, str_line))
        punctuation_count = len(re.findall('[,.\\-\'":?!]', str_line))
        output_file.write(f"Line: {i+1}: {str_line} ({letters})({punctuation_count})\n")

