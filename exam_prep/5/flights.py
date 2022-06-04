def flights(*args):
    flight_info = {}
    for ind in range(0, len(args), 2):
        if args[ind] == "Finish":
            break
        else:
            destination = args[ind]
            if destination not in flight_info:
                flight_info[destination] = 0
            flight_info[destination] += args[ind+1]
    return flight_info


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco',
              98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215,
              'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300,
              'Sydney', 0))
