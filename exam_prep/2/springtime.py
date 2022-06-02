def start_spring(**kwargs):
    flowers = {}
    result = ''
    for key, value in kwargs.items():
        if value not in flowers:
            flowers[value] = []
        flowers[value].append(key)
    sorted_flowers = sorted(flowers.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for key, value in sorted_flowers:
        result += f"{key}:\n"
        sorted_value = sorted(value)
        for item in sorted_value:
            result += f"-{item}\n"
    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

