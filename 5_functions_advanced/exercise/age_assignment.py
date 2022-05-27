def age_assignment(*args, **kwargs):
    result = ''
    people = {}
    for key, value in kwargs.items():
        for arg_ind in range(len(args)):
            if args[arg_ind][0] == key:
                people[args[arg_ind]] = value

    sorted_people = sorted(people.items(), key=lambda kvp: kvp[0])
    for name, age in sorted_people:
        result += f"{name} is {age} years old.\n"
    return result





print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
