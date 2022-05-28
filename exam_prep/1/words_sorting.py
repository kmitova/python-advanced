def words_sorting(*args):
    word_sums = {}
    total_sum = 0
    result = ''
    for el in args:
        ascii_sum = 0
        for sym in el:
            ascii_sum += ord(sym)
        word_sums[el] = ascii_sum
        total_sum += ascii_sum

    if total_sum % 2 == 0:
        sorted_words = sorted(word_sums.items(), key=lambda kvp: kvp[0])
    else:
        sorted_words = sorted(word_sums.items(), key=lambda kvp: -kvp[1])

    for key, value in sorted_words:
        result += f"{key} - {value}\n"
    return result


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




