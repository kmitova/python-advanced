def shopping_list(budget, **kwargs):
    result = ''
    # no_space = False
    if budget < 100:
        return "You do not have enough budget."
    items = 0
    for key, value in kwargs.items():
        price = float(value[0])
        quantity = int(value[1])
        if price * quantity <= budget:
            items += 1
            budget -= price * quantity
            result += f"You bought {key} for {price * quantity:.2f} leva.\n"
        if items == 5:
            # no_space = True
            break
    return result

print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
