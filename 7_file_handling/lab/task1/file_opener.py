try:
    file = open('text.txt')
    print("File found")
    print(file.readlines())
except FileNotFoundError:
    print('File not found')

# could also use os.path.exists method and if/ else
