import os


# paths
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'data.txt')

close_to_open = {')': '(', ']': '[', '}': '{', '>': '<'}

# Part 1
def part1():
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    total = 0

    for line in open(filename, 'r'):
        stack = []

        for char in list(line.strip()):
            if char in close_to_open.values():
                stack.append(char)
            elif not stack or stack.pop() != close_to_open[char]:
                total += points[char]
                break
    print(total)


part1()