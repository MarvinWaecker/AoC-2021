import os


# paths
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'data.txt')

### Solution 1

# load data
data = []
with open(filename, 'r') as file:
    for x in file.read().splitlines():
        data.append(x.split())

# part 1
def part1(horiz, depth):
    for order in data:
        if order[0] == 'forward':
            horiz += int(order[1])
        elif order[0] == 'up':
            depth -= int(order[1])
        elif order[0] == 'down':
            depth += int(order[1])
        else:
            print('no valid order sir')
    print(horiz*depth)

# part 2
def part2(horiz, depth, aim):
    for order in data:
        if order[0] == 'forward':
            horiz += int(order[1])
            depth += aim*int(order[1])
        elif order[0] == 'up':
            aim -= int(order[1])
        elif order[0] == 'down':
            aim += int(order[1])
        else:
            print('no valid order sir') 
    print(horiz*depth)

part1(0, 0)
part2(0, 0 , 0)





# Solution 2 (shorter)
with open(filename, 'r') as file:
    data = [x.split() for x in file.read().splitlines()]
aim, x1, y1, x2, y2 = 0, 0, 0, 0, 0
move = {
    'forward' : lambda aim, x, y, z, part : (aim, x + z, y) if part == 1 else (aim, x + z, y + (z * aim)),
    'down'    : lambda aim, x, y, z, part : (aim, x, y + z) if part == 1 else (aim + z, x, y),
    'up'      : lambda aim, x, y, z, part : (aim, x, y - z) if part == 1 else (aim - z, x, y)
    }
for instruction, amt in data:
    aim, x1, y1 = move[instruction](aim, x1, y1, int(amt), 1)
    aim, x2, y2 = move[instruction](aim, x2, y2, int(amt), 2)
print(x1 * y1)  
print(x2 * y2) 







