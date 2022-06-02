from collections import deque

flowers = ['rose', 'tulip', 'daffodil', 'lotus']
word_found = False
vowels = deque(input().split())
consonants = input().split()
word = ''
while vowels and consonants:
    vowel = vowels[0]
    consonant = consonants[-1]
    for i in range(len(flowers)):
        for el in flowers[i]:
            if el == vowel:
                flowers[i] = flowers[i].replace(el, "")
            if el == consonant:
                flowers[i] = flowers[i].replace(el, "")
        if flowers[i] == '':
            word_found = True
            break
    vowels.popleft()
    consonants.pop()
    if word_found:
        break
if flowers[0] == '':
    word = 'rose'
elif flowers[3] == '':
    word = 'lotus'
elif flowers[2] == '':
    word = 'daffodil'
elif flowers[1] == '':
    word = 'tulip'
if word_found:
    print(f'Word found: {word}')
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
