def start_spring(**kwargs):
    plants = {}
    result = ''
    for key, value in kwargs.items():
        if value not in plants:
            plants[value] = []
        plants[value].append(key)

    sorted_plants = sorted(plants.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for key, value in sorted_plants:
        result += f"{key}:\n"
        sorted_values = sorted(value)
        for el in sorted_values:
            result += f"-{el}\n"

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
