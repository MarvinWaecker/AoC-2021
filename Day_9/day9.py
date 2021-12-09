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
    neighbors_lower = []
    for pos in get_neighbours(x,y):
        if map.get(pos, 9) > map[(x, y)]:   # return 9 if there's no neighbor
            neighbors_lower.append(True)
        else:
            neighbors_lower.append(False)
    return all(neighbors_lower)

def get_low_points():
    lows = []
    for x, y in map:
        if is_low_point(x, y):
            lows.append((x,y))
    return lows




#part2
def get_basin(pos):
    basin = {pos}
    follow_path(pos, basin)
    return basin

def follow_path(pos, basin):
    p1 = map[pos]    # current position value
    for neighbour in get_neighbours(*pos):  # loop through neighbours of current position 
        p2 = map.get(neighbour, 0)          # get neighbour value (return 0 if there's no neighbour so it's a water point)
        if p2 > p1 and p2 != 9:             # if neighbour value is higher than current position value and neighbour value is not 9 (doesn't count)
            basin.add(neighbour)            # add neighbour to basin
            follow_path(neighbour, basin)   # run again with neighbour as current position


p = 1
basins = []
for pos in get_low_points():
    basin = get_basin(pos)
    basins.append(len(basin))
for basin in sorted(basins)[-3:]:
    p *= basin


print(f"Part 1 : {sum(map[pos] + 1 for pos in get_low_points())}")
print(f"Part 2 : {p}")