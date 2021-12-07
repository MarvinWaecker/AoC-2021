import os


# paths
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'data.txt')

from functools import reduce
from more_itertools import split_at
from collections import defaultdict
from itertools import chain, dropwhile

def parse_bingo_line(line, row):
    return {
        val : (row, idx) for idx, val in enumerate(map(int, line.split()))
    }

def parse_bingo(lines):
    return reduce(
        dict.__or__, 
        (parse_bingo_line(line, row) for row, line in enumerate(lines)),
        {})

def comp(pred):
    return lambda x: not pred(x)

def parse_multiple_bingos(lines):
    return [parse_bingo(block) for block in split_at(lines, comp(bool))]
    
def parse_input(filename):
    with open(filename) as f:
        nums = list(map(int, next(f).strip().split(",")))
        return nums, parse_multiple_bingos(dropwhile(comp(bool), map(str.strip, f)))

def is_bingo(nums, board):
    indices = list(filter(lambda x: x is not None,
        (board.get(num, None) for num in nums)))
        
    row_dict = defaultdict(set)
    col_dict = defaultdict(set)

    for x, y in indices:
        row_dict[x].add(y)
        col_dict[y].add(x)

    return any(len(s) == 5 for s in chain(row_dict.values(), col_dict.values()))

def find_first_bingo(nums, boards):
    for idx in range(len(nums)):
        curr = nums[:idx]
        try:
            return curr, next(board for board in boards if is_bingo(curr, board))
        except:
            pass
    
def calculate_final_score(nums, board):
    return sum(set(board) - set(nums)) * nums[-1]

def part_1(filename):
    called_nums, winning_board = find_first_bingo(*parse_input(filename))
    return calculate_final_score(called_nums, winning_board)

def find_last_bingo(nums, boards):
    for idx in range(len(nums)):
        boards = [board for board in boards if not is_bingo(nums[:idx], board)]
        if len(boards) == 1:
            return find_first_bingo(nums, boards)

def part_2(filename):
    called_nums, losing_board = find_last_bingo(*parse_input(filename))
    return calculate_final_score(called_nums, losing_board)