def concatenate(*args, **kwargs):
    concat_args = ''
    for el in args:
        concat_args += el

    for key, value in kwargs.items():
        if key in concat_args:
            concat_args = concat_args.replace(key, value)
    return concat_args


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
