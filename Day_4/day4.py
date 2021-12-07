import os


# paths
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'test_data.txt')


# load data
numbers = []
with open(filename, 'r') as file:
    for k, line in enumerate(file.read().splitlines()):
        if not line.isspace():
            if k == 0:
                numbers = line.strip().split(',')
            else:
                boards = line.split()







from itertools import chain

# load data
with open(filename, 'r') as file:
    numbers, *data = file.read().strip().split("\n\n")

nums = numbers.split(',')
nums = [int(n) for n in nums]

boards = []
for board in data:
    rows = board.split("\n")
    rows_new = []
    cols = []
    for row in rows:
        # print(row)
        row = [int(x) for x in row.split()]

        # print(set(row))
        rows_new.append(row)
    boards.append(rows_new)

lines = []
for i in range(len(boards)):
    for j in range(len(boards[i][0])): 
        line = []
        for k in range(len(boards[i])): 
            line.append(boards[i][j][k])
        # boards[i].append(line)
        lines.append(line)

for board in boards:
    for i in range(len(board)):
        board.append(lines[i])

print(len(boards))
print(boards[2])
for b in boards:
    print(b)


# drawn, remain = set(), set(range(len(boards)))

# for num in nums:
#     drawn.add(num)
#     for i in set(remain):
#         print(drawn)
#         if any(set(line) <= drawn for line in boards[i]):
#             print('test1')
#             remain.remove(i)
#             if len(remain) == len(boards)-1 or not remain:
#                 print('test')
#                 print(num * sum(set.union(set(*boards[i])) - drawn))




# boards = []
# for board in data:
#     rows = [
#         [int(x) for x in row.split()]
#         for row in board.split("\n")
#     ]
#     # fmt:on
#     boards.append([set(line) for line in chain(rows, zip(*rows))])




# drawn, remaining = set(), set(range(len(boards)))
# print(remaining)
# for number in map(int, numbers.split(",")):
#     drawn.add(number)

#     for i in set(remaining):
#         if any(set(line) <= drawn for line in boards[i]):
#             remaining.remove(i)

#             if len(remaining) == len(boards) - 1 or not remaining:
#                 print(number * sum(set.union(*boards[i]) - drawn))







