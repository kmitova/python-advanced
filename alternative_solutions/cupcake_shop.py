def stock_availability(flavors, command, *args):
    if command == 'delivery':
        for el in args:
            flavors.append(el)
    elif command == 'sell':
        if args:
            if str(args[0]).isnumeric():
                flavors = flavors[args[0]:]
            else:
                for flavor in args:
                    if flavor in flavors:
                        flavors = [i for i in flavors if i != flavor]
        else:
            flavors.pop(0)
    return flavors


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
