nums = (float(el) for el in input().split())  # using () to make a tuple of float

dictionary = {}

for num in nums:
    if num not in dictionary:
        dictionary[num] = 0
    dictionary[num] += 1

for key, value in dictionary.items():
    print(f"{key} - {value} times")

