import os


# paths
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'data.txt')

data = {}
with open(filename, 'r') as file:
    for x, pos in enumerate(file.read().split(',')):
        data[x] = int(pos) 

def get_cheapest(data):
    minimum = min(data.values())
    maximum = max(data.values())

    fuel_list = []
    for i in range(minimum, maximum + 1):
        all_fuel = 0
        for x in data.values():
            fuel_used = abs(x - i)
            all_fuel += fuel_used
        # print(all_fuel)
        fuel_list.append(all_fuel)
    return fuel_list

print(min(get_cheapest(data)))
