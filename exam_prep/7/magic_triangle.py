def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    row2 = [1, 1]
    previous_row = row2
    for i in range(n-2):
        row = []
        for i in range(0, len(previous_row)-1):
            row.append(previous_row[i] + previous_row[i+1])
        row.insert(0, 1)
        row.append(1)
        triangle.append(row)
        previous_row = row
    return triangle


get_magic_triangle(5)
