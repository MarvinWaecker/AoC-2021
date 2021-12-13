import os


# paths
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'test_data.txt')


# load data
# numbers = []
# data = []
# with open(filename, 'r') as file:
#     for k, line in enumerate(file.read().splitlines()):
#         if not line.isspace():
#             if k == 0:
#                 numbers = line.strip().split(',')
#             else:
#                 data.append(line.split('\n\n'))


# # load data
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


drawn, remaing_boards = set(), set(range(len(boards)))

print(nums)

for num in nums:    # loop though all numbers that will be drawn
    drawn.add(num)  # add number to drawn list
    for i in set(remaing_boards):   # loop trough remaining boards 
        print(drawn)
        if any([set(line) <= drawn for line in boards[i]]):   # check if drawn number is higher or equal to any number in board
            remaing_boards.remove(i)    # remove board
            if len(remaing_boards) == len(boards)-1 or not remaing_boards:
                print(num * sum(set.union(*[set(row) for row in boards[i]]) - drawn))


