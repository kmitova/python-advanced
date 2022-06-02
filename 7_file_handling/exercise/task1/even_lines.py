symbols = ["-", ",", ".", "!", "?"]

with open('text.txt') as file:
    for i, line in enumerate(file):
        if i % 2 == 0:
            result = ' '.join(reversed(line.strip().split()))
            for sym in symbols:
                result = result.replace(sym, '@')

            print(result)
