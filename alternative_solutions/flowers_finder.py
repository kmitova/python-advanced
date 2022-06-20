from collections import deque

rose = set('rose')
tulip = set('tulip')
daffodil = set('daffodil')
lotus = set('lotus')
word_found = False

vowels = deque([x for x in input().split()])
consonants = [x for x in input().split()]

while vowels and consonants:
    if vowels[0] in rose:
        rose.remove(vowels[0])
    if consonants[-1] in rose:
        rose.remove(consonants[-1])
    if vowels[0] in tulip:
        tulip.remove(vowels[0])
    if consonants[-1] in tulip:
        tulip.remove(consonants[-1])
    if vowels[0] in lotus:
        lotus.remove(vowels[0])
    if consonants[-1] in lotus:
        lotus.remove(consonants[-1])
    if vowels[0] in daffodil:
        daffodil.remove(vowels[0])
    if consonants[-1] in daffodil:
        daffodil.remove(consonants[-1])
    vowels.popleft()
    consonants.pop()

    if len(rose) == 0:
        print("Word found: rose")
        word_found = True
        break
    if len(lotus) == 0:
        print("Word found: lotus")
        word_found = True
        break
    if len(tulip) == 0:
        word_found = True
        print("Word found: tulip")
        break
    if len(daffodil) == 0:
        word_found = True
        print("Word found: daffodil")
        break


if not word_found:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(x for x in vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(x for x in consonants)}")

