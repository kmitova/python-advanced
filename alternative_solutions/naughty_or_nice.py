def naughty_or_nice_list(kids, *args, **kwargs):
    nice_kids = []
    naughty_kids = []
    not_found = []

    for el in args:
        info = el.split('-')
        num = int(info[0])
        status = info[1]
        needed_num = None
        count = 0
        sought_kid = ''
        for item in kids:
            if item[0] == num:
                count += 1
        if count == 1:
            needed_num = num
        for item in kids:
            if item[0] == needed_num:
                sought_kid = item[1]
                if status == 'Nice':
                    nice_kids.append(sought_kid)
                elif status == 'Naughty':
                    naughty_kids.append(sought_kid)
                kids.remove(item)
                break

    if kwargs:
        for key, value in kwargs.items():
            name = key
            status = value
            count = 0
            sought_kid = ''
            for item in kids:
                if item[1] == name:
                    count += 1
            if count == 1:
                sought_kid = name
                # needed_num = num
            for item in kids:
                if item[1] == sought_kid:
                    # sought_kid = item[1]
                    if status == 'Nice':
                        nice_kids.append(sought_kid)
                    elif status == 'Naughty':
                        naughty_kids.append(sought_kid)
                    kids.remove(item)
                    break
    if kids:
        for el in kids:
            if el[1] not in nice_kids or el[1] not in naughty_kids:
                not_found.append(el[1])
    result = ''
    if nice_kids:
        result += f"Nice: {', '.join(nice_kids)}\n"
    if naughty_kids:
        result += f"Naughty: {', '.join(naughty_kids)}\n"
    if not_found:
        result += f"Not found: {', '.join(not_found)}\n"
    return result






print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
