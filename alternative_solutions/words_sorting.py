def words_sorting(*args):
    words = {}
    result = ''
    for el in args:
        el_sum = sum([ord(x) for x in el])
        words[el] = el_sum
    if sum(words.values()) % 2 != 0:
        sorted_words = sorted(words.items(), key=lambda kvp: -kvp[1])
    else:
        sorted_words = sorted(words.items())

    for key, value in sorted_words:
        result += f"{key} - {value}\n"
    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
