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


boards_num = len(boards)
row_num = len(boards[0])
col_num = len(boards[0][0])


lines = []
boards_new = boards
for i in range(boards_num):
    for j in range(col_num): 
        line = []
        for k in range(row_num): 
            line.append(boards[i][k][j])
        # boards[i].append(line)
        boards_new[i].append(line)


drawn, remain = set(), set(range(len(boards)))

for num in nums:
    drawn.add(num)
    for i in set(remain):
        if any(set(line) <= drawn for line in boards[i]):
            remain.remove(i)
            if len(remain) == len(boards)-1 or not remain:
                print(num * sum(set.union(*[set(row) for row in boards[i]]) - drawn))


