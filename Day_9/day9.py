import os


# paths
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'data.txt')

map = {}
with open(filename) as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line.strip()):
            map[(x, y)] = int(char)

#part1
def get_neighbours(x, y):
    return {(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)}

def is_low_point(x, y):
    return all(map.get(pos, 9) > map[(x, y)] for pos in get_neighbours(x, y))

def get_low_points():
    return [(x, y) for x, y in map if is_low_point(x, y)]

print("Part 1:")
print(sum(map[pos] + 1 for pos in get_low_points()))