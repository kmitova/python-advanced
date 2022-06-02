def naughty_or_nice_list(names, *args, **kwargs):
    result = ''
    santa_list = {}
    nice_kids = []
    naughty_kids = []
    not_found_kids = []
    for pair in names:
        if pair[0] not in santa_list:
            santa_list[pair[0]] = []
        santa_list[pair[0]].append(pair[1])

    if args:
        for item in args:
            data = item.split('-')
            num = int(data[0])
            kind = data[1]
            for key in santa_list:
                if key == num and len(santa_list[key]) == 1:
                    name = santa_list[key][0]
                    if kind == "Nice":
                        nice_kids.append(name)
                    else:
                        naughty_kids.append(name)
                    santa_list[key].remove(name)

    if kwargs:
        for key, value in kwargs.items():
            count = 0
            for k, v in santa_list.items():
                for el in v:
                    if el == key:
                        count += 1
            for k, v in santa_list.items():
                if key in santa_list[k]:
                    # print(count)

                    if count == 1:
                        if value == "Nice":
                            nice_kids.append(key)
                        elif value == "Naughty":
                            naughty_kids.append(key)
                        santa_list[k].remove(key)

    if len(santa_list) > 0:
        for key, value in santa_list.items():
            if value:
                for el in value:
                    not_found_kids.append(el)

    if nice_kids:
        result += f"Nice: {', '.join(nice_kids)}\n"
    if naughty_kids:
        result += f"Naughty: {', '.join(naughty_kids)}\n"
    if not_found_kids:
        result += f"Not found: {', '.join(not_found_kids)}\n"

    return result


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy")

    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty"
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
