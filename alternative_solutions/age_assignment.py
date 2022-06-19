def age_assignment(*args, **kwargs):
    result = ''
    result_dict = {}
    for el in args:
        if el[0] in kwargs:
            key = el[0]
            value = kwargs[key]
            kwargs[el] = value
            result_dict[el] = value

    sorted_result_dict = sorted(result_dict.items())
    for key, value in sorted_result_dict:
        result += f"{key} is {value} years old.\n"
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
