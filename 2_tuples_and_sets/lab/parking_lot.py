n = int(input())
cars = set()
for i in range(n):
    direction, car = input().split(", ")
    if direction == "IN":
        cars.add(car)
    elif direction == "OUT":
        cars.remove(car)
if cars:
    print("\n".join(cars))
else:
    print("Parking Lot is Empty")
